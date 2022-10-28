from Employee import Employee


# this class inherits the properties of Employee class which inherited the properties of
# the Person class
class HourlyEmployee(Employee):
    def __init__(self, f_name, l_name, ssn, employee_id, hourly_pay, hours_per_week):
        super().__init__(f_name, l_name, ssn, employee_id)
        self.hourly_pay = hourly_pay
        self.hours_per_week = hours_per_week

    # return weekly_pay which is hourly_pay * hours_per_week
    def get_weekly_pay(self):
        return self.hourly_pay * self.hours_per_week

    # str function that will display f_name, l_name, snn, employee_id, and weekly_pay
    def __str__(self):
        return f'{super().__str__()} Paycheck: {self.get_weekly_pay()}'

