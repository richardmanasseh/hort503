# Example of a program split into small logical functional units, each perfroming a task

# Case: program to calculate and display the net pay and name of every employee in a company

# Algorithm:
# Step 1 Define your problem (as above).
# Step 2 Algorithms input(s): employee record
# Step 3  Define the algorithm's (input and output) variables:
# Step 4 Outline the algorithm's operation(s): # calculate pay
                                               # 4.1 calculate gross pay
                                               # 4.2 calculate deductions
                                               # 4.3 calculate net pay
                                               # 4.4 print wage slip
# Step 5 Output the results (output) of your algorithm's operations:  display your favourite quote on screen
                                                                # display the name of the person who said it on nect line
# Possible program modules (each with one or more parameters, but just ONE return value as the ideal) # easier to test. Note: not they way in object-oriented programming
    # def get_employee_record(name, ):
    # def calc_net_pay(gross_pay, deductions):
    # def calc_gross_pay(pay_rate, hours_worked):
    # def calc_deductions(gross_pay, tax details):
    # def issue_wage_slips():
    # def display_wage_slip(employee_name, net_pay):

def calc_gross_pay(pay_rate, hours_worked): # By decomposing the program, this module (function) can now be coded and tested independently

    # Algorithm:
        # Step 1 Define your problem (as above).
        # Step 2 Algorithms input(s): pay_rate, hours_worked
        # Step 3 Define the algorithm's local (input and output) variables: gross_pay
        # Step 4 Outline the algorithm's operation(s): gross_pay = pay_rate * hours_worked.
        # Step 5 Output the results (output) of your algorithm's operation(s): gross_pay
        # Step 6 Develop test plan ( testing program) to prove this module will behave correctly as a python function
    gross_pay = gross_pay = pay_rate * hours_worked

    return gross_pay

# The Testing Program: requires three variables: employee_pay_rate, employee_hours, and employee_gross_pay
employee_pay_rate = float(input("Please enter the employee pay rate "))
employee_hours = float(input("Please enter the hours worked by the employee "))
employee_gross_pay = cal_gross_pay(employee_pay_rate, employee_hours) # calls our original function calc_gross_pay, with employee_pay_rate, employee_hours as the arguments
print("The employee's gross pay is $ " + format(employee_gross_pay, ".2f")) # formatted to two decimal places

# Algorithm:
    # Step 1 Define your problem (as above).
    # Step 2 Algorithms input(s):employee_pay_rate, employee_pay_rate
    # Step 3 Define the algorithm's local (input and output) variables: employee_pay_rate, employee_hours, and employee_gross_pay
    # Step 4 Outline the algorithm's operation(s): # obtain the pay pay rate
                                                   # obtain the hours worked
                                                   # calculate the gross pay
                                                   # display the gross pay
    # Step 5 Output the results (output) of your algorithm's operation(s): display of employ gross pay


def display_wage_slip(employee_name, net_pay): # Note: function with formal parameters and no return value
    # Algorithm:
        # Step 1 Define your problem (as above).
        # Step 2 Algorithms input(s): employee_name, net_pay
        # Step 3 Define the algorithm's local (input and output) variables: none
        # Step 4 Outline the algorithm's operation(s): display of employ name and net pay
        # Step 5 Output the results (output) of your algorithm's operation(s): display of employ name and net pay
        # Step 6 Return value = none
    print("WAGE SLIP")
    print("NAME:", name)
    print("NET PAY:", format(net_pay, ".2f"))
    print()

    # With no return value, the Testing Program: requires only two variables: employee_name, net_pay
    employee_name = input("Please enter name of employee: ")
    employee_net_pay = float(input("Please enter net pay of employee: "))
    display_wage_slip(employ_name, employee_net_pay) # call to the function, with the actual arguments
