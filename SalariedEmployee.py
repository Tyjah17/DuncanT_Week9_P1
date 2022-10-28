from Employee import Employee


# this class inherits the properties of Employee class which inherits the properties of
# the Person class
class SalariedEmployee(Employee):
    def __init__(self, f_name, l_name, ssn, employee_id, monthly_salary):
        super().__init__(f_name, l_name, ssn, employee_id)
        self.monthly_salary = monthly_salary

    # returns monthly_salary depending on user input
    def get_monthly_salary(self):
        return self.monthly_salary

    # str function that will display f_name, l_name, snn, employee_id, and monthly_salary
    def __str__(self):
        return f'{super().__str__()} Salary: ${"{:.2f}".format(self.get_monthly_salary())}'
