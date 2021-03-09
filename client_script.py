from account import Account
from employee import Employee
from customer import Customer
from savings_account import Savings_account
from current_account import Current_account
#Employee and Customer classes both inherit from Person class
#each greeting method is encapsulated in the relevant class
#Inheriting Employee from Person is polymorphism as we are changing the data type
jessie = Employee("Jessie", "auguste", "1234", "2")
asia = Customer("Asia", "Sharif", "23", "3454354")
print(jessie.greeting())
print(asia.greeting())
jessie_savings = Savings_account(500, 2.5, 3, 2)
jessie_savings.withdraw(300)
print(jessie_savings.getbalance())
jessie_savings.withdraw(500)

asia_current = Current_account(1000, -500, 500)
print(asia_current.getbalance())
print(asia_current.send_money(100, "jessie"))
print(asia_current.getbalance())
print(asia_current.send_money(3000, "jackie"))
print(asia_current.receive_money(50, "jessie"))
print(asia_current.getbalance())