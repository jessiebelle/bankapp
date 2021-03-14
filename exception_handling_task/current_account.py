from insufficient_funds_exception import InsufficientFunds
from account import Account


class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft, spend_limit):
        Account.__init__(self, name, balance) # changed from super to account.__init___
        self._overdraft = overdraft
        self._spend_limit = spend_limit # move to the exceptions

    def __str__(self):
        super().__str__()
        #return "{}'s bank balance is {:.2f} withdrawal fee: {} sort code: {} account number: {}".format(self._name,
        #    self._balance, self._overdraft, self._spend_limit, self._sortcode, self._account_number)
        return f"{self._name}'s bank balance is {self._balance:.2f}, overdraft:{self._overdraft}, spend limit: {self._spend_limit}, sort code: {self._sortcode}, account number: {self._account_number}"


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

        if amount > self._balance:
            raise InsufficientFunds("transaction denied to withdraw: " + str(amount))
        else:
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


