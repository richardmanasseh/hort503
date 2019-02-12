# Making Scripts that Decide Things: If, else, elif
# Case:
    # Write a prograam that asks users to enter their age.
        # If they are 18 years or older the program reports back their age and asks them to collect their polling card
        # If they enter their age as 17 the program reports abck their age and informs them that they can vote next year
        # However, if they are not olde enough to vote (=18+) and are not 17, the program again reports back their age but this time tells them that they are too young to vote
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
    print("You are" str(age), + "so collect your polling card")
elif age == 17:
    print("You are" str(age), + "so you can vote next year")
else:
    print("You are" str(age), + "so you are too young to vote")
