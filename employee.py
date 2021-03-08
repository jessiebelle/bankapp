from person import Person

class Employee(Person):
    level_of_access = "full access"
    def __init__(self, first_name, surname, employee_id):
        super().__init__(first_name, surname)
        self.employee_id = employee_id