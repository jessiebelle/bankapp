from account import Account


class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate, withdrawal_limit, withdrawal_number):
        Account.__init__(self, name, balance)
        self._interest_rate = interest_rate
        self._withdrawal_limit = withdrawal_limit
        self.withdrawal_number = withdrawal_number

    def __str__(self):
        super().__str__()
        return f"{self._name}'s bank balance is {self._balance:.2f}, interest rate: {self._interest_rate}, " \
               f"withdrawal fee: {self._withdrawal_limit}, sort code: {self._sortcode}, account number: {self._account_number}"


    def withdraw(self, amount):
        if self.withdrawal_number < self._withdrawal_limit and amount - self._balance > 0:
            self._balance -= amount
            self.withdrawal_number = self.withdrawal_number + 1
            print(f"You have successfully withdrawn £{amount}, your new balance is {self._balance}")
        else:
            print(f"You have reached your limit of {self._withdrawal_limit} withdrawals this month")


if __name__ == "__main__":
    account4 = SavingsAccount("Johnny", 25000, 1.25, 2500, 3)
    print(account4)