from insufficient_funds_exception import InsufficientFunds
from account import Account


class CurrentAccount(Account):
    def __init__(self, balance, overdraft, spend_limit):
        self._balance = balance
        self._overdraft = overdraft
        self._spend_limit = spend_limit

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
        if amount > balance:
            raise InsufficientFunds
        else:
            self._balance -= amount

if __name__ == "__main__":
    a1 = CurrentAccount(100, -200, 500)
    print(a1.make_withdrawal(150))