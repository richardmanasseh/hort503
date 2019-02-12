# If...
# else ... credit a bonus to the account

# Algorithm:
    # Step 1 Define your problem: we apply charges or credit bonus to a bank account
    # Step 2 Algorithms input(s):employee_pay_rate, employee_pay_rate
    # Step 3 Define the algorithm's local (input and output) variables: employee_pay_rate, employee_hours, and employee_gross_pay
    # Step 4 Outline the algorithm's operation(s): # set bank charge
                                                   # set bank bonus
                                                   # set account balance
                                                   # determine whether or not account is overdrwan
                                                   # apply the charge/credit the bonus
                                                   # display the account balance
    # Step 5 Output the results (output) of your algorithm's operation(s): display the account balance

# Process representation in Python code
bank_charge = 10
bank_bonus = 1
account_balance = 50

if account_balance < 0:
    account_balance = account_balance - bank_charge
else:
    account_balance = account_balance + bank_charge
print("The account balance is:", + str(account_balance))


bank_charge = 10
bank_bonus = 1
account_balance = -20

if account_balance < 0:
    account_balance = account_balance - bank_charge
else:
    account_balance = account_balance + bank_charge
print("The account balance is:", + str(account_balance)) # output of script execution
