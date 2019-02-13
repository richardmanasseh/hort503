# Names, variables, codes, functions
# A function is a block of re-usable code to perform specific tasks, which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function always return data as a result, unless the function is a procedure which returns nothing
# When you define a function, you specify the name and the sequence of statements.# def my_function()
# Later, you can "call" the function by name when you want to run (or use) it.
# you can create a function by using the keyword def (=define) followed by the parameter(s) in ( ), a colon :, and then finally an indented function body:
# the indentation says "the following statements belong to this function"
# So functions become the building blocks of a programs
# Name a function so name tells you what its going to do, and the object it's doing it to.
# this one is like your scripts with argv

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}") # how far you indentate doesn't matter, but you must do it
    print("How are you today?")           # the tab size varies between computers, so it's best to use the space key

greet("Claire", "Mutesi") # we're calling the function greet, the actual value for each parameter specified
greet("Amake", "Edna")
greet("Atiki", "Able")

# Packing and Unpacking Arguments:
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(*my_list) # fun(my_list) doesnt work; TypeError: fun() missing 3 required positional arguments: 'b', 'c', and 'd'
# meaning typeError: fun() takes exactly 4 arguments (1 given)
# We can use * to unpack the list so that all elements of it can be passed as different argumeents.


def print_two(*args): # in this case we have just named the function "print_two"; name of your function will be in blue text in your script
                      # the input you define for your function (here, *args) is called a parameter
                      # whereas an argument is the actual value for a given parameter
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
