# Ex 5: More Variables and Printing
# You can also embed or insert a variable into a string by putting it inside {}
# You also must start the string with the letter f for ”format”. e.g. print(f"Hello {somevar}")
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}) and {my_weight} I get {total}.")