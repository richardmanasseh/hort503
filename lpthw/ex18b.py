# Python Default Arguments for functions

def multi_display(message = 'default', times = 2):
    for i in range(times):
        print(message)

multi_display() # no arguments passed, so value of 2 assigned to 'times' will be the one in the range function
                # consequuently, this loop is going to execute (output the string default) twice


def multi_display(message = 'default', times):
    for i in range(times):
        print(message)

multi_display()


def multi_display(message = 'default', times = 2): # here, we have assigned (=) default values to the parameters "message" and 'times'
                                                   # Always, parameters with default values must be placed at the END of the parameter list
    for i in range(times):
        print(message)

multi_display('hello world', times = 5) # default values overwritten 5X


def multi_display(message = 'default', times = 2):
    for i in range(times):
        print(message)

multi_display(times = 7) # we've not given any argument capable of overwiting default message, so default gets printed 7X


def multi_display(message = 'default', times = 2):
    for i in range(times): # times value at default retained
        print(message)

multi_display(message = 'hello world') # keyword argument set to "hello world" overwites default message 2x


def multi_display(message = 'default', times = 2):
    for i in range(times): # times value at default retained
        print(message)

multi_display('hello world', times = 3) # positional argument set to "hello world", followed by keyword argument, overwites default message 3x


def multi_display(message = 'default', times = 2):
    for i in range(times): # times value at default retained
        print(message)

multi_display(message = 'hello world', 3) # "hello world" is a keyword argument, 3 is a positional argument # Syntax Error: non-keyword argument after keyword argument


def addNumbers(*num): # we're defining a function that adds a series of numbers, but we donot know how many numbers are there in advance
                      # the * allows us to pass a variable number of arguments to the function...
                      # this is known as a non-keyworded variable argument list
    sum = 0
    for i in num:
        sum = sum + 1
    print(sum)
addNumbers(1, 2, 3, 4, 5)
addNumbers(1, 2, 3, 4, , 6, 7, 8, 9)
