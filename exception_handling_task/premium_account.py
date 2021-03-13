from account import Account


class PremiumAccount(Account):
    def __init__(self, name, balance, withdrawal_fee, interest):
        Account.__init__(self, name, balance) # changed from super to account.__init___git 
        self.withdrawal_fee = withdrawal_fee
        self.interest = interest
        self.withdrawals = 0

    def __str__(self):
        super().__str__()
        return f"{self._name}'s bank balance is {self._balance:.2f} withdrawal fee: {self.withdrawal_fee}, interest: " \
               f"{self.interest}, withdrawals: {self.withdrawals}, sort code: {self._sortcode}, account number: {self._account_number}"

    def make_withdrawal(self, amount):
        self._balance -= amount
        self.withdrawals += 1
        if self.withdrawals > 3:
            self._balance -= int(self._withdrawal_fee)


    def make_deposit(self, amount):
        self._balance += amount
        if amount < 1000:
            self._balance += amount * self.interest
        else:
            self._balance += 1000 * self.interest


if __name__ == "__main__":
    Michelle = PremiumAccount("Michelle", 10000, 3, 0.05)
    print(Michelle)
