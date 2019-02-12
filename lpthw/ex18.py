# Names, Variables, Codes, Functions
# A function is a block of re-usable code to perform a specific task, which only runs when it is called.
# You can pass data, known as parameters, into a function, and when you do, the function always returns as a result.
# When you define a function, you specify the name and the sequence of statements.# def my_function()
# Later, you can "call" the function by name when you want to run (or use) it.
# you can create a function by using the keyword def (=define), as def nameoffunction(first_parameter, last_parameter): (colon), and then finally an indented function body:
    # the indentation says "the following statements belong to this function"
    # So functions become the building blocks of a programs
# Name a function so name tells you what its going to do, and the object it's doing it to.
# Functions allow a program to be split into small logical functional units, each perfroming a task
# A program (software system) developed with functions is much easier to debug than a large "monolithic" program developed without functions

# Here is the syntax template of a value-returning function prototype:
# def nameoffunction(first_parameter, last_parameter): # these parameters are aka "default" arguments
	# Statement(s)
	    #.
	    #.
	    #.
	# return value-returning-expression

# Example: Value-returning Function
def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit """
    return (T_in_celsius * 9 / 5) + 32
for t in (22.6, 25.8, 27.3, 29.8):
    print(t, ": ", fahrenheit(t))

def greet(first_name, last_name): # define a function "greet" that does the following with parameters 'first_name' and 'last_name':
    print(f"Hi {first_name} {last_name}") # how far you indentate doesn't matter, but you must do it
    print("How are you today?")           # the tab size varies between computers, so it's best to use the space key

greet("Claire", "Mutesi") # we're calling the function greet, the actual value for each parameter specified; they overwrite the default arguments in a positional sense
greet("Amake", "Edna")
greet("Atiki", "Able")

# Packing and Unpacking Arguments:
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(*my_list) # fun(my_list) doesnt work; TypeError: fun() missing 3 required positional arguments: 'b', 'c', and 'd'
              # meaning typeError: fun() takes exactly 4 arguments (1 given)
              # We can use * to unpack the list so that all elements of it can be passed as different argumeents.

def print_two(*args): # we've another function "print_two"; # *args to pass a variable number of arguments to a function than you previously defined.
                      # the input you define for your function (here, *args) is called a parameter
                      # an argument is the actual value for a given parameter
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments, so is a Void Function
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# Another Example: Function with no arguments but return value


# Another Example: Void Function
# A function defined w/o input parameter(s) has no return value, and is called a procedure:

def copyright_display(): # takes no input parameters...
    print("This software is copyrighted to WSU")
    print()
    print("The development team are: ")
    print("Richard Manassseh")
    print("Lindani Moyo")
    print("Hanu Papu")

copyright_display() #... therefore you call it without arguments
