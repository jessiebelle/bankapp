from account import Account
from insufficient_funds_exception import InsufficientFunds
from max_number_withdrawals import MaxNumberOfWithdrawals


class PremiumAccount(Account):
    def __init__(self, name, balance, withdrawal_fee, interest_rate):
        Account.__init__(self, name, balance)
        self._withdrawal_fee = withdrawal_fee
        self._interest_rate = interest_rate
        self._num_of_withdrawals = 1

    def __str__(self):
        super().__str__()
        return f"{self._name}'s bank balance is {self._balance:,.2f} withdrawal fee: {self._withdrawal_fee:.2f}, interest: " \
               f"{self._interest_rate}, withdrawals: {self._num_of_withdrawals}, sort code: {self._sortcode}," \
               f" account number: {self._account_number}"

    def make_withdrawal(self, amount):
        if self._balance < amount:
            raise InsufficientFunds("Error: Insufficient funds to withdraw:£" + str(amount))
        elif self._num_of_withdrawals > 3:
            raise MaxNumberOfWithdrawals("Error: You have withdrawn 3 times already")
        self._balance -= (amount + int(self._withdrawal_fee))
        self._num_of_withdrawals += 1

    def make_deposit(self, amount):
        self._balance += amount
        if amount < 1000:
            self._balance += amount * self._interest_rate
        else:
            self._balance += 1000 * self._interest_rate


if __name__ == "__main__":
    michelle = PremiumAccount("Michelle Bloggs", 50, 3, 0.05)
    try:
        michelle.make_withdrawal(500)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(michelle.get_balance())
    try:
        michelle.make_withdrawal(5)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(michelle.get_balance())
    try:
        michelle.make_withdrawal(5)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(michelle.get_balance())
    try:
        michelle.make_withdrawal(5)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(michelle.get_balance())
    try:
        michelle.make_withdrawal(5)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(michelle.get_balance())

