import random
# import abc ? to make metaclass


class Account:
    number_created = 0

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._sortcode = "21 21 21"
        self._account_number = random.randint(10000000, 99999999)
        Account.number_created += 1

    def __str__(self):
         return f"{self._name}'s bank balance is {self._balance:.2f}, sort code: {self._sortcode}, account number: {self._account_number}"

    def get_sortcode(self):
        return self._sortcode

    def get_account_num(self):
        return self._account_number

    def make_deposit(self, amount):
        self._balance += amount

    def make_withdrawal(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance
