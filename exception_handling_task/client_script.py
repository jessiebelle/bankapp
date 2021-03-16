from insufficient_funds_exception import InsufficientFunds
from max_number_withdrawals import MaxNumberOfWithdrawals
from current_account import CurrentAccount
from savings_account import SavingsAccount
from premium_account import PremiumAccount

# Current account
account1 = CurrentAccount("Nina", 2000, -500, 200)
print(account1)
a1 = CurrentAccount("Michael Smith", 10, -200, 500)
print(a1)

try:
    a1.make_withdrawal(50)
except InsufficientFunds as my_error:
    print(str(my_error))

print(a1.get_balance())
# adding a built in exception
try:
    a1.make_withdrawal("fifty")
except TypeError as type_error:
    print("Error:" + str(type_error))
print(a1)
print("-" * 30)
# Premium account
account2 = PremiumAccount("Ben", 10000, 3, 0.05)
print(account2)
print("-" * 30)

michelle = PremiumAccount("Michelle Bloggs", 50, 3, 0.05)
print(michelle)
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
print("Your account balance is: £" + str(michelle.get_balance()))
print("-" * 30)

# Savings account
account3 = SavingsAccount("Sally", 500000, 2.50, 3.25, 5)
print(account3)
print("-" * 30)
account4 = SavingsAccount("Jonny Cash", 50, 0.5, 5, 4)
print(account4)

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
    print("your account balance is" + str(self.balance))

try:
    account4.make_withdrawal(30)
except MaxNumberOfWithdrawals as max_error:
    print(str(max_error))
except InsufficientFunds as my_error:
    print(str(my_error))
print("Your account balance is: £" + str(account4.get_balance()))




