# parent class for the class Employee
class Person:
    def __init__(self, f_name, l_name, ssn):
        self.f_name = str(f_name)
        self.l_name = str(l_name)
        self.ssn = str(ssn)
    #
    def __str__(self):
        return f'Name: {self.f_name} {self.l_name} SSN: {self.ssn}'
