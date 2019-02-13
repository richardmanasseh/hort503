# print function interpretes/processes a math script following PEMDAS
# in PEMDAS, % has the same precedence as MD; 10%3 read "10 mod 3"=1
print("I will now count my chickens:")
#Start with hens, then roosters, then eggs
print("Hens" , 25.0 + 30.0 / 6.0)
print("Roosters" , 100.0 - 25.0 * 3.0 % 4.0)
#remember PEMDAS applies
print("Now I will count the eggs:")
# PEMDAS applies
# expression could have been more readable if broken by parentheses
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)
# Examples of Inequalities processed as True or False
print("Is it true that 3.0 + 2.0 < 5.0 - 7.0?") # prints as a question
print(3.0 + 2.0 < 5.0 - 7.0) # returns as False

# Why the above inequality is False:
print("What is 3.0 + 2.0?", 3.0 + 2.0)
print("What is 5.0 - 7.0?", 5.0 - 7.0)

print("Oh, that's why it's False")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0) # processes 5.0 > -2.0 as True or False
print("Is it greater or equal?", 5.0 >= -2.0) # processes 5.0 >= -2.0 as True or False
print("Is it less or equal?", 5.0 <= -2.0) # processes 5.0 <= -2.0 as True or False

# you can also store numbers in variables:
my_number = 10
print(my_number)
# we can also convert this variable into a string; this is handy if you want to print numbers next to strings
print(str(my_number))
print(str(my_number), "my favorite number.")
