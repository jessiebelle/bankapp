from insufficient_funds_exception import InsufficientFunds
from account import Account


class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft, spend_limit):
        Account.__init__(self, name, balance)
        self._overdraft = overdraft
        self._spend_limit = spend_limit

    def __str__(self):
        super().__str__()
        return f"{self._name}'s bank balance is {self._balance:.2f}, overdraft:{self._overdraft:.2f}, spend limit: " \
               f"{self._spend_limit:.2f}, sort code: {self._sortcode}, account number: {self._account_number}"

    def send_money(self, amount, recipient):
        if amount < self._spend_limit:
            self._balance -= amount
            return f"you have sent £{amount} to {recipient}"
        else:
            return f"Could not send £{amount} to {recipient}, as it is larger than your spending limit of £{self._spend_limit}"

    def receive_money(self, amount, recipient):

        self._balance += amount
        return f"you have received £{amount} from {recipient}"

    def make_withdrawal(self, amount):
        if (self._balance - amount) <= self._overdraft:
            raise InsufficientFunds("transaction denied to withdraw: " + str(amount))
        self._balance -= amount


if __name__ == "__main__":
    a1 = CurrentAccount("Michael", 10, -200, 500)
        # a1.make_withdrawal(150)
    print(a1)
    try:
        a1.make_withdrawal(50)
    except InsufficientFunds as my_error:
            print(str(my_error))
    print(a1.get_balance())
# adding a built in exception
    try:
        a1.make_withdrawal("fifty")
    except TypeError as type_error:
        print("Error:" + str(type_error))
    print(a1)


