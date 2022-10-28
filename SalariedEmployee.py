from Employee import Employee

# 
class SalariedEmployee(Employee):
    def __init__(self, f_name, l_name, ssn, employee_id, monthly_salary):
        super().__init__(f_name, l_name, ssn, employee_id)
        self.monthly_salary = monthly_salary
    # returns users monthly salary
    def get_monthly_salary(self):
        return self.monthly_salary
    # display user first and last name, employee_id and monthly_salary
    def __str__(self):
        return f'{super().__str__()} Salary: ${"{:.2f}".format(self.get_monthly_salary())}'
