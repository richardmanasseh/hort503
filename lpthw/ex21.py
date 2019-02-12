# Functions Can Return Something
# The print() function writes, i.e., "prints", a string in the console.
# The return statement causes your function to exit and hand back a value to its caller.
def add(a, b): # this (add) function is called with two parameters: a and b
    print(f"ADDING {a} + {b}") # we print what our function is doing
    return a + b # the summation of a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5) # call the add function, and set it to variable "age"
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # making function calls inside functions

print("That becomes: ", what, "Can you do it by hand?")
