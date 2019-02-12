# Ex 4: Variables and Names
# Variables are "words" that hold a value
FRUIT = peach #
    # The operand to the left of the = operator (FRUIT) is the name of the variable
    # The operand to the right (peach) is the value stored in the variable.
    # A variable is similar to the memory functionality found in most calculators, in that it holds one value which can be retrieved many times
# you to assign a single value to several variables simultaneously. e.g:
a = b = c = 1 # Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location
#You can also assign multiple objects to multiple variables e.g:
a,b,c = 1,2,"john" # Here, two integer objects with values 1 and 2 are assigned to variables a and b respectively, and one string object with the value "john" is assigned to the variable c.

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are" , cars , "cars available.")
print("There are only" , drivers , "drivers available.")
print("There will be" , cars_not_driven , "empty cars today.")
print("We can transport" , carpool_capacity , "people today.")
print("We have" , passengers , "to carpool today.")
print("We need to put about" , average_passengers_per_car , "in each car.")
