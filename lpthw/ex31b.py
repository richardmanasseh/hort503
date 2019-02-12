# Making Scripts that Decide Things: If, else, elif
if...
else ... credit a bonus to the account

# Algorithm:
    # Step 1 Define your problem: we apply charges to a bank account if the account is overdrawn
    # Step 2 Algorithms input(s):employee_pay_rate, employee_pay_rate
    # Step 3 Define the algorithm's local (input and output) variables: employee_pay_rate, employee_hours, and employee_gross_pay
    # Step 4 Outline the algorithm's operation(s): # set bank charge
                                                   # set bank bonus
                                                   # set account balance
                                                   # determine whether or not account is overdrwan
                                                   # apply the charge/credit the bonus
                                                   # display the account balance
    # Step 5 Output the results (output) of your algorithm's operation(s): display the account balance

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
print("The account balance is:", + str(account_balance))


print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")    # Question to user

door = input("> ") # > just used as an input indicator for the end user, could use any other.

if door == "1": # == in door == 1 will check if the value stored in variable door is equal to 1.
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
