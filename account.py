class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance
        
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        print(f"You have successfully withdrawn £{amount}, your new balance is {self._balance}")

    def get_balance(self):
        return f"Your current balance is £{self._balance}"
