from insufficient_funds_exception import InsufficientFunds
from account import Account


class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft, spend_limit):
        super().__init__(self, balance)
        self._balance = balance
        self._overdraft = overdraft
        self._spend_limit = spend_limit # move to the exceptions

    def __str__(self):
        super().__str__()
        return "{}'s bank balance is {:.2f} withdrawal fee: {} sort code: {} account number: {}".format(self._name,
            self._balance, self._overdraft, self._spend_limit, self._sortcode, self._account_number)

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
        try:
            if amount > self._balance:
                raise InsufficientFunds(amount)
        finally:
            self._balance -= amount


if __name__ == "__main__":
    a1 = CurrentAccount("Michael", 100, -200, 500)
    a1.make_withdrawal(150)
    print(a1)


