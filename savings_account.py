from account import Account


class Savings_account(Account):
    def __init__(self, initial_balance, interest_rate, withdrawal_limit, withdrawal_number):
        self._balance = initial_balance
        self._interest_rate = interest_rate
        self._withdrawal_limit = withdrawal_limit
        self.withdrawal_number = withdrawal_number

    def withdraw(self, amount):
        if self.withdrawal_number < self._withdrawal_limit:
            self._balance -= amount
            self.withdrawal_number = self.withdrawal_number + 1
        else:
            print(f"You have reached your limit of {self._withdrawal_limit} withdrawals this month")
    def getbalance(self):
        return self._balance
