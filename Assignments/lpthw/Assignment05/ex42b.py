# A Python Class in Code:
    # Has a ClassName, Class attributes, and Class methods
# Case: A program that controlls the movement of money in and out of a bank account:
    # A sensible ClassName would be BankAccount
    # A typical attribute would be balance (attribute aka state)...an atribute is essentially a variable
    # A typical method (aka behavior) would be debit, this is where you decide to withdraw some money...
    # and you have a method that allows that withdrawal to take place and it debits the balance...
    #... a method is essentially a function
    # attributes and methods are aka members of the class
    # an instance of this class (called an object) is created as my_instance_1 = ClassName()

# To create the class, we write:
class BankAccount:
    """This is a demo class""" # What the class is about
    pass # used to indicate where your code will eventually go but has not yet been written
         # the pass statement is a null operation and nothing happens when it executes

def demo_method(self): # self is the parameter that picks up the Id of whatever object...
                       # this method becomes tied to.
    print("This is a demo method for debit")
    print("The id of self is", id(self))

my_instance_1 = BankAccount() # the constructor line, constructs an instance of the Class
print(type(my_instance_1))
print(id(my_instance_1)) # object's unique identifier

my_instance_2 = BankAccount()
print(type(my_instance_2))
print(id(my_instance_2))

# Assigning a Python Object # two objects are the same thing
my_instance_3 = my_instance_1
print(type(my_instance_3))
print(id(my_instance_3)) # same as for my_instance_1

print(BankAccount.__doc__) # returns what the class is about
print(my_instance_1.__doc__) # also returns what the class is about
print(dir(BankAccount)) # returns the members of the class
print(dir(my_instance_1)) # returns the same members

print(dir(BankAccount)) # returns the members of the class, including the demo_method

print("The id of the first object is", id(my_instance_1)")
print("The id of the second object is", id(my_instance_2)")
my_instance_1.demo_method() # method is called to my_instance_1
my_instance_2.demo_method() # method is called to my_instance_1

# Ex 42: Creating a Class, say, a Staff class
# This Class can be used to store all the relevant information about a staff in the company
# To create the class, we write:

class Staff: # we capitalize each first letter in the name
    # within the class, we can declare two variables to store the name and position of the Staff
    # in addition, we can also code a method (a function) called calculatePay() to calculate the pay of the staff
    # if a function exists within a class, it is more commonly referred to as a method
    # next, we define a special method called __init__ for the class. This is known as the initializer of the class
    # frequently, the initializer is used to initialize the variables (give them initial values) in the class
    def __init__(self, pPosition, pName, pPay):
            self.position = pPosition # position, name, pay are the class's instance variables and are pre-fixed with the keyword "self"...
            self.name = pName         # and are initialized by assigning pPosition, pName, pPay to them
            self.pay = pPay
            print('Creating Staff Object')

    # the other special method that is commonly included when we code a class is __str__
    def __str__(self):
        # we use it to return a human readable string that represents the class
        # in this example, we have used it to return a string that gives the values of the three instance variables
        return "Position = %s, Name = %s, Pay = %d" %(self.position, self.name, self.pay)

    # Next is the calculatePay() method:
    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name) # we have not prefixed "self to the variables prompt, hours, hourlyRate...
        hours = input(prompt)                                           #...because they are local variables and exist...
        prompt = 'Enter the hourly rate for %s: ' %(self.name)          # ..only within the calculatePay() method
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate) # we calculate the pay and assign the result to the instance variable self.pay...
        return self.pay                       #  and return the value of self.pay


## ??
harry = Halibut()
