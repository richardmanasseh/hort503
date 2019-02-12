# Python Nested Selection Constructs: an if nested within an else
# Write a prograam that asks users to enter their age. If they are old enough to vote the program asks them to collect their polling card
# However, if they are not old enough the program tells them that they are too young to vote
# Algorithm:
        # Step 1 Define your problem:
        # Step 2 Algorithms input(s):user age
        # Step 3 Define the algorithm's local (input and output) variables:
        # Step 4 Outline the algorithm's operation(s): # obtain user's age
                                                       # set bank bonus
                                                       # set account balance
                                                       # determine whether or not user is >=18
                                                       # if True, apply the charge
                                                       # display decision
        # Step 5 Output the results (output) of your algorithm's operation(s): # collect your polling card
                                                                                # you are too young to vote

age = int(input("Please enter your age  "))
if age >= 18:
    print("collect your polling card")
else:
    print("you are too young to vote")


# Ammendment: If the user enters their age as 17, they are still told that they are too young to vote, but in addition they are told they can vote next year
# Algorithm:
        # Step 1 Define your problem:
        # Step 2 Algorithms input(s):user age
        # Step 3 Define the algorithm's local (input and output) variables:
        # Step 4 Outline the algorithm's operation(s): # obtain user's age
                                                       # determine whether or not user is >=18
                                                       # if True, display # collect your polling card
                                                       # if False,# you are too young to vote, and ask if age == 17
        # Step 5 Output the results (output) of your algorithm's operation(s): # collect your polling card
                                                                                # you are too young to vote
                                                                                # you can vote next year

age = int(input("Please enter your age  "))
if age >= 18:
    print("collect your polling card")
else:
    print("you are too young to vote") # and...
    if age == 17:
        print("you can vote next year")

# Program Test Plan
# Within the program there are two selection constructs:
        # age >= 18, with boundary 18
        # age == 17, with boundary 17
# We therefore need to have a test plan that includes 16,17, 18,19
        Input(age)          Expected output              Actual Output          Pass            Fail
        16                  # you are too young to vote

        17                  # you are too young to vote
                            # you can vote next year
        18                  # collect your polling card
        19                  # collect your polling card

age = int(input("Please enter your age  "))
if age >= 18:
    print("collect your polling card")
else:
    print("you are too young to vote") # and...
    if age == 17:
        print("you can vote next year")
