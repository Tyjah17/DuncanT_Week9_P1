import unittest

from SalariedEmployee import SalariedEmployee
from HourlyEmployee import HourlyEmployee

if __name__ == '__main__':
    # unittest.main()
    # ask user if they get paid by salary or hourly
    hourly_or_salary = input("Are you payed by Hour(Enter H) or Salary(Enter S): ")
    # if salary
    if hourly_or_salary == "S" or hourly_or_salary == "s":
        # get user information
        f_name = str(input('Enter first name: '))
        l_name = str(input('Enter last name: '))
        ssn = str(input('Enter SSN: '))
        id_num = int(input('Enter ID: '))
        salary = float(input('Enter monthly salary: '))
        # store user information as an object
        p = SalariedEmployee(f_name, l_name, ssn, id_num, salary)
        # print user information
        print(p)
    # if hourly
    elif hourly_or_salary == "H" or hourly_or_salary == "h":
        # get user information
        f_name2 = str(input('Enter first name: '))
        l_name2 = str(input('Enter last name: '))
        ssn2 = str(input('Enter SSN: '))
        id_num2 = int(input('Enter ID: '))
        pay = float(input("Enter hourly pay: "))
        hours = float(input("Enter hours worked: "))
        # store user information
        p2 = HourlyEmployee(f_name2, l_name2, ssn2, id_num2, pay, hours)
        # print user information
        print(p2)
