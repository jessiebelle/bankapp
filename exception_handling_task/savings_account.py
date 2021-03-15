from account import Account
from insufficient_funds_exception import InsufficientFunds
from max_number_withdrawals import MaxNumberOfWithdrawals


class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate, withdrawal_num_limit, num_of_withdrawals):
        Account.__init__(self, name, balance)
        self._interest_rate = interest_rate
        self._withdrawal_num_limit = withdrawal_num_limit
        self._num_of_withdrawals = num_of_withdrawals

    def __str__(self):
        super().__str__()
        return f"{self._name}'s bank balance is {self._balance:.2f}, interest rate: {self._interest_rate}, " \
               f"number of withdrawals limit: {self._withdrawal_num_limit}, sort code: {self._sortcode}, account number: {self._account_number}"

    def make_withdrawal(self, amount):
        if self._withdrawal_num_limit < self._num_of_withdrawals:
            raise MaxNumberOfWithdrawals("Error: You have reached your limit of " + str(self._withdrawal_num_limit) +
                                         " withdrawals this month")
        elif amount - self._balance >= 0:
            raise InsufficientFunds("Error: Insufficient funds to withdraw:£" + str(amount))
        else:
            self._balance -= amount
            self._num_of_withdrawals += 1


if __name__ == "__main__":
    account4 = SavingsAccount("Jonny Cash", 50, 0.5, 5, 4)
    try:
        account4.make_withdrawal(15)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(account4.get_balance())
    try:
        account4.make_withdrawal(60)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(account4.get_balance())
    try:
        account4.make_withdrawal(30)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    print(account4.get_balance())
    try:
        account4.make_withdrawal(30)
    except MaxNumberOfWithdrawals as max_error:
        print(str(max_error))
    except InsufficientFunds as my_error:
        print(str(my_error))
    # account4.make_withdrawal(5)
    # print(account4.get_balance())
    # account4.make_withdrawal(5)
    # print(account4.get_balance())
    # account4.make_withdrawal(5)
    # print(account4.get_balance())