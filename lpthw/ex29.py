# What If
# At the end of each working day,the balance of a bank account is considered...
# IF the account is overdrawn, charges are applied to the account.
# So we ask the question: is the account overdrawn? Yes (=True) or No (=False)
# Algorithm:
        # Step 1 Define your problem: we apply charges to a bank account if the account is overdrawn
        # Step 2 Algorithms input(s):account_balance, bank_charge
        # Step 3 Define the algorithm's local (input and output) variables: account_balance
        # Step 4 Outline the algorithm's operation(s): # set bank charge
                                                       # set bank bonus
                                                       # set account balance
                                                       # determine whether or not account is overdrwan
                                                       # if True, apply the charge
                                                       # display the account balance
        # Step 5 Output the results (output) of your algorithm's operation(s): display the account balance.

set bank_charge = 10
set account_balance = 100
if account_balance < 0:
    account_balance = account_balance - bank_charge # indentation typically four spaces

print("The account balance is" + str(account_balance))


set bank_charge = 10
set account_balance = -10
if account_balance < 0:
    account_balance = account_balance - bank_charge # indentation typically four spaces

print("The account balance is" + str(account_balance))


people = 20
cats = 30
dogs = 15

if people < cats: # if this Boolean expression is True, execute the "branch" code under it; otherwise skip it.
    print("Too many cats! The world is doomed!") # this branch code has to be indented with four spaces to tell the block defined by the Boolean expression.
                                                 # Python expects you to indent something after you end a line with ":"

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5 # <=> 15 dogs + 5 = 20 dogs. += can be considered an "increment operator"

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
