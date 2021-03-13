from account import Account


class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate, withdrawal_limit, withdrawal_number):
        super().__init__(self, name, balance)
        self._interest_rate = interest_rate
        self._withdrawal_limit = withdrawal_limit
        self.withdrawal_number = withdrawal_number

    def __str__(self):
        super().__str__()
        return "{}'s bank balance is {:.2f} withdrawal fee: {} sort code: {} account number: {}".format(self._name,
            self._balance, self._interest_rate, self._withdrawal_limit, self.withdrawal_number,
            self._sortcode, self._account_number)

    def withdraw(self, amount):
        if self.withdrawal_number < self._withdrawal_limit and amount - self._balance > 0:
            self._balance -= amount
            self.withdrawal_number = self.withdrawal_number + 1
            print(f"You have successfully withdrawn £{amount}, your new balance is {self._balance}")
        else:
            print(f"You have reached your limit of {self._withdrawal_limit} withdrawals this month")

if __name__ == "__main__":
    account4 = SavingsAccount(25000, 1.25, 2500, 3)