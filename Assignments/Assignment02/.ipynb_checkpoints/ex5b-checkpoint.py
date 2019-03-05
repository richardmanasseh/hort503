myname = 'Richard'
myage = 35 # not a lie
myheight = 74 # inches
myweight = 180 # lbs
myeyes = 'Blue'
myteeth = 'White'
myhair = 'Brown'
mynewweight = myweight / 2.2 # kg, as 1kg = 2.2lbs
mynewheight = myheight / 2.54 # cm, as 1inch = 2.54cm

print(f"Let's talk about {myname}.")
print(f"He's {mynewweight} centimeters tall.")
print(f"He's {mynewweight} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {myeyes} and {myhair} hair.")
print(f"His teeth are usually {myteeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
total = myage + mynewheight + mynewweight
print(f"If I add {myage}, {mynewheight}) and {mynewweight} I get {total}.")
