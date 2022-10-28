from Person import Person


# this class inherits properties f_name, l_name, and ssn from Person class
# a new property employee_id is made
class Employee(Person):
    def __init__(self, f_name, l_name, ssn, employee_id):
        super().__init__(f_name, l_name, ssn)
        self.employee_id = employee_id

    # prints first and last name, ssn and employee id
    def __str__(self):
        return f'{super().__str__()}, ID: {self.employee_id}'
