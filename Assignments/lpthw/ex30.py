# Else and If: If --> Elif--> Else
people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people: # elif = else if, triggerd if cars > people is False.
                    # If the condition for if is False, it checks the condition of the next if

    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars: # prevents short-circuiting
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.") # triggerd if people < trucks.
