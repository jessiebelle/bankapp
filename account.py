class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance
        
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def getbalance(self):
        return self._balance
