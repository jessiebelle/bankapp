from person import Person
from datetime import date
class Employee(Person):
    level_of_access = "full access"
    def __init__(self, first_name, surname, age, employee_id):
        super().__init__(first_name, surname, age)
        self.employee_id = employee_id


    def greeting(self):
        return f"Hi {self.first_name}, welcome back to work. Your employee number is {self.employee_id}"

    def get_profile(self):
        return f"Name: {self.first_name} {self.surname}\nAge: {self.age}\nEmployee ID:{self.employee_id} "


