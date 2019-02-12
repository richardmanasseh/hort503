# Defining Your own Functions
# Problem: we want to determine if a given number is a prime number
# Considerations:
    # A prime number is a whole number greater than 1 whose only factors are 1 and itself.
    # whose only factors are 1 and itself, means can divide into itself and 1 with remainder 0
    # so function should be able to:
        # check if number is greater than 1 i.e. range >=2
        # check that can divide into itself and 1 with remainder 0

def CheckIfPrime(NumbertoCheck): # Function has one parameter, NumbertoCheck, which is just a variable used to store the arguments
                                  # we pass to the function
    for x in range(2, NumbertoCheck):
        if (NumbertoCheck%x == 0):
            return False
    return True

answer = CheckIfPrime(13)


# Local and Global Variable Scope
product = 0 #

def find_product(number1, number2):
    product = number1 * number2 # read R-L: the product of number1 and number2 is assigned to this local product
                                # this product is only available durring the runtime of this function
    print("The LOCAL variable product is:" , product)
    return product # executes 3rd; it will return the value of the local variable product (6), and return/pass it to....

print('The GLOBAL product variable BEFORE the call is:', product) # executed first
product = find_product(2, 3) # call to function, which executes second, only when it's called   ....to here
print('The GLOBAL product variable AFTER the call is:', product) # executes 4th, which has just had the 6 returned to it


# Local and Global Variable Scope
product = 0 #

def find_product(number1, number2):
    result = number1 * number2 # read R-L: the product of number1 and number2 is assigned to this local product
                                # this product is only available durring the runtime of this function
    print("The LOCAL variable result is:" , result)
    return result # executes 3rd; it will return the value of the local variable product (6), and return/pass it to....

print('The GLOBAL product variable BEFORE the call is:', product) # executed first
product = find_product(2, 3) # call to function, which executes second, only when it's called   ....to here
print('The GLOBAL product variable AFTER the call is:', product) # executes 4th, which has just had the 6 returned to it by the function

# Local and Global Variable Scope
product = 0 #

def find_product(number1, number2):
    result = number1 * number2 # read R-L: the product of number1 and number2 is assigned to this local product
                                # this product is only available durring the runtime of this function
    print("The LOCAL variable result is:" , result)
    print('The GLOBAL product value is:', product) # will output its value as 0, since this function has access to both its local variable and any global variables
    return result # executes 3rd; it will return the value of the local variable product (6), and return/pass it to....

print('The GLOBAL product variable BEFORE the call is:', product) # executed first
product = find_product(2, 3) # call to function, which executes second, only when it's called   ....to here
print('The GLOBAL product variable AFTER the call is:', product) # executes 4th, which has just had the 6 returned to it by the function
# print("The LOCAL variable result is:" , result) # Error: result variable not defined, because it has a local scope.
