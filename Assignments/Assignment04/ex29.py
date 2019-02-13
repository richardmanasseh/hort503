# What if
people = 20
cats = 30
dogs = 15


if people < cats: # if this Boolean expression is True, execute the "branch" code under it; otherwise skip it.
    print("Too many cats! The world is doomed!") # this code has to be indented with four spaces to tell what lines of code are in the block defined by the Boolean expressionself.
    # Python expects you to indent something after you end a line with :

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
