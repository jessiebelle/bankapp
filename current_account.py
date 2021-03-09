from account import Account


class Current_account(Account):
    def __init__(self, initial_balance, overdraft, spend_limit):
        self._balance = initial_balance
        self._overdraft = overdraft
        self._spend_limit = spend_limit

    def send_money(self, amount, recipient):
        if amount < self._spend_limit:
            self._balance -= amount
            print(f"you have sent £{amount} to {recipient}")
        else:
            print(f"Could not send £{amount} to {recipient}, as it is larger than your spending limit of £{self._spend_limit}")

    def receive_money(self, amount, recipient):

        self._balance += amount
        print(f"you have received £{amount} from {recipient}")
