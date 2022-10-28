from Person import Person

# this class is a child class of the class Person
class Employee(Person):
    def __init__(self, f_name, l_name, ssn, employee_id):
        super().__init__(f_name, l_name, ssn)
        self.employee_id = employee_id

    def __str__(self):
        return f'{super().__str__()}, ID: {self.employee_id}'
