from insufficient_funds_exception import InsufficientFunds
from account import Account
from current_account import CurrentAccount
from savings_account import SavingsAccount
from premium_account import PremiumAccount

# Current account
account1 = CurrentAccount("Nina", 2000, -500, 200)
print(account1)


# Premium account
account2 = PremiumAccount("Ben", 10000, 3, 0.05)
print(account2)

# Savings account
account3 = SavingsAccount("Sally", 500000, 2.50, 3.25, 5)
print(account3)


