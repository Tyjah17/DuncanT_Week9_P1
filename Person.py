# parent class for the class Employee
class Person:
    # Person Constructor
    def __init__(self, f_name, l_name, ssn):
        self.f_name = str(f_name)
        self.l_name = str(l_name)
        self.ssn = str(ssn)

    # prints first and last name along with ssn
    def __str__(self):
        return f'Name: {self.f_name} {self.l_name} SSN: {self.ssn}'
