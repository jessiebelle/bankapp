from person import Person

class Customer(Person):
    level_of_access = "mid level access"
    def __init__(self, first_name, surname, age, customer_number):
        super().__init__(first_name, surname, age)
        self.customer_number = customer_number

    def greeting(self):
        return f"Hi {self.first_name}, welcome back to our bank. Your customer number is {self.customer_number}"