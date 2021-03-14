from account import Account
from insufficient_funds_exception import InsufficientFunds, MaxNumberOfWithdrawals
# from max_num_withdrawals_exception import MaxNumberOfWithdrawals


class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate, max_withdrawal_num, num_of_withdrawals):
        Account.__init__(self, name, balance)
        self._interest_rate = interest_rate
        self._max_withdrawal_num = max_withdrawal_num
        self._num_of_withdrawals = num_of_withdrawals

    def __str__(self):
        super().__str__()
        return f"{self._name}'s bank balance is {self._balance:.2f}, interest rate: {self._interest_rate}, " \
               f"withdrawal fee: {self._max_withdrawal_num}, sort code: {self._sortcode}, account number: {self._account_number}"

    def make_withdrawal(self, amount):
        if self._max_withdrawal_num < self._num_of_withdrawals:
            raise MaxNumberOfWithdrawals("Error: You have reached your limit of " + str(self._max_withdrawal_num) +
                                         " withdrawals this month")
        elif amount - self._balance >= 0:
            raise InsufficientFunds("Error: Insufficient funds to withdraw:£" + str(amount))
        else:
            self._balance -= amount
            self._num_of_withdrawals += 1

    # def make_withdrawal(self, amount):
    #
    #     if self._max_withdrawal_num < self._num_of_withdrawals:
    #         raise MaxNumberOfWithdrawals("You have reached your limit of " + str(self._max_withdrawal_num) +
    #                                      " withdrawals this month")
    #     elif amount - self._balance <= 0:
    #         raise InsufficientFunds("transaction denied to withdraw: " + str(amount))
    #     else:
    #         self._balance -= amount
    #         self._num_of_withdrawals += 1


#to replace else statement, we want to raise an exception when a person has hit their withdrawal limit.

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