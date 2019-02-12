# Functions and variables
# Illustrates all the different ways we're able to give a function the values it needs when we call it
# Global variable: is available to every function, therefore usually not included under a function block, which has local variables
def cheese_and_crackers(cheese_count, boxes_of_crackers): # could be renamed print_snack_inventory
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # Here, we call the function giving/passing it numbers directly: an object that contains number 20 and another object containing number 30

# We can yet pass the numbers through variables:
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
