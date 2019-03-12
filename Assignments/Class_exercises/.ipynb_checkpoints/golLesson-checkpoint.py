Designing a Python Class from a Given Specification (Desccription)
'''whenever a customer joins a bank, an account is created in their name
and a balance is set based on how much they deposit. the account must also
allow for a deposit to credit (alter by adding to) the account and for a withdrawal to debit the
account. Upon request the balance of the account and the name of the customer
will be returned. Also once an account is created the name of the customer can
be changed.'''

    Do a word-by-word verb and noun 'analysis' of the Specification
        a verb conveys an action whch we can think of as a behavior or a method to perform the action
        a nown is the name of something, state of existance i.e. an attribute
        so a nown has an associated action
        narrow down especially to words that occur more than once in the Specification

    Possible list: '''customer bank, account created name balance set deposit
    deposit credit withdrawal debit request returned changed.'''

    Now use the list and your understanding of the specification to derive a Class model:
    Based on the specification, Account would be a good class name
    What would be the data fields of the account?
        balance (of the account)
        name (of the customer)
    What would be the methods of the account?
        __init__(self, balance, method)
        credit(self, deposit) (will do something to/increase the balance,
                        and needs to know by how much it will alter the balance, i.e. needs a parameter,
                        which is the deposit)
        debit(self, withdrawal) (will do another thing to/reduce the balance,
                        and needs to know by how much it will reduce the balance, i.e. needs a parameter,
                        which is the withdrawal))
        get_balance(self) (will return whatever the balance is of the account at any particular time)
        get_name(self) (will return the name of the customer)
        set_name(self, name) (will allow change of the name of the customer)

`   Now convert model into code:`
class Account:
    def __init__(self, balance, name):
        sell.balance = balance
        self.name = name

    def credit(self, deposit):
        self.balance = self.balance + deposit # functionailty of the method

    def debit(self, withdrawal):
         self.balance = self.balance - withdrawal

    # Now the Python getter and setter Methods:

    def get_balance(self):
        return self.balance # returs value stored in self.balance

    def get_name(self):
        return self.name

    def set_name(self, name): # used to (re-)set name
        self.name = name

# Now let's create an Instance of the Python Class....

customer = Account(0, "Rita Jones")
# and test whether the methods defined in the class work when they're instances of the class:

print(customer.get_name(), 'has a balance of ', customer.get_balance())
customer.credit(100)
print(customer.get_name(), 'has a balance of ', customer.get_balance()) # customer.name could give us direct access to the attribute name w/o the need for a get_name method
customer.debit(45)
print(customer.get_name(), 'has a balance of ', customer.get_balance()) # customer.balance ==> possible to not need getter and setter methods
customer.set_name(Rita Hartley)
print(customer.get_name(), 'has a balance of ', customer.get_balance())


# Now the Python getter and setter Methods:

def get_balance(self):
    return self.balance # returs value stored in self.balance

def get_name(self):
    return self.name

def set_name(self, name): # used to (re-)set name
    self.name = name

# Now let's create an Instance of the Python Class....

customer = Account(0, "Rita Jones")
# ==> possible to not need getter and setter methods...:

print(customer.name, 'has a balance of ', customer.balance())
customer.credit(100)
print(customer.name, 'has a balance of ', customer.balance()) # customer.name could give us direct access to the attribute name w/o the need for a get_name method
customer.debit(45)
print(customer.name, 'has a balance of ', customer.balance()) # customer.balance
customer.name = "Rita Hartley"
print(customer.name, 'has a balance of ', customer.balance())

# so Python Why Data Hiding? i.e. have data fields accessed indirectly through the relatively "exposed" methods?
    ==> protect against infringement/manipulation
Pythons Data Hiding Convention
    ==> python doesnt have keywords e.g. 'private' to hide data fields
    ==> we can use __ (double underscore) to hide a data field
class Account:
    def __init__(self, balance, name):
        sell.__balance = balance
        self.name = name

    def credit(self, deposit):
        self.__balance = self.__balance + deposit # functionailty of the method

    def debit(self, withdrawal):
         self.__balance = self.__balance - withdrawal

    # Now the Python getter and setter Methods:

    def get_balance(self):
        return self.__balance # returs value stored in self.balance

    def get_name(self):
        return self.name

    def set_name(self, name): # used to (re-)set name
        self.name = name

print(customer.name, 'has a balance of ', customer.__balance()) # would return an error msg
customer.credit(100)
print(customer.name, 'has a balance of ', customer.__balance()) #
print(customer.name, 'has a balance of ', customer.__balance()) #
customer.name = "Rita Hartley"
print(customer.name, 'has a balance of ', customer.__balance())

python is dynamic, meaning the object can change during runtime (as the program is executing)

class Cell(self, x, y, state):

ClassName: BankAccount
Class Attribute(s), aka States, variables: e.g. balance, name of customer
Class Behavior(s), aka Methods: Methods, Program statements, or Functions (e.g. debit) that give you access to (eg read()), set the values of, the variables
An instance of the class (aka Object) would be, my_account1 = ClassName(), meaning my_account is assigned ClassName
Attributes and Behaviors are collectively called Members of the class or object created
my_account1 = ClassName() # this is called a Constructor line, because it just constructed/established an instance of the class
my_account2 = ClassName() # this also just constructed/established another instance of the class
print(type(my_account1))
print(id(my_account1))

print(type(my_account2))
print(id(my_account2))

print(dir(ClassName)) # will print members of the class
print(dir(my_account1)) # will print members of the class ClassName
print(my_account1.__doc__) # would return the Class's documentation string

my_account3 = my_account1 # here we're ASSIGNING the object my_account1 to my_account3, so both will be pointing to (or are bound to) the same object
print(type(my_account3)) # same as for my_account1
print(id(my_account3)) # same as for my_account1

class Cell:
    def debitmethod(self): # we're defining a method/function within the class, self is there to tie the method to whichever object/instance of this Class is created         print(id(self))
        print('mitosis')

print(dir(Cell)) # will return the members list that will now include the 'debitmethod'
mycell = Cell()
print(dir(myCell)) # will return the members list that will now include the 'debitmethod', which mycell inherits from the class
print(id(mycell)
mycell.debitmethod()

class Cell:
    def debitmethod(self): # the self is there to recieve the id of each instance created based on the Class
        print('mitosis')
        print('the id of self is', id(self))

mycell_1 = Cell()
mycell_2 = Cell()
print('the id of the first object is', id(mycell_1))
print('the id of the second object is', id(mycell_2))
mycell_1.debitmethod()
mycell_2.debitmethod()

Python Method Parameters and self
class Cell:
    def double_it(self, value): # the self is there to recieve the id of the instance, value will recieve the 2, without self it will crash
        doubled_value = value * 2
        return doubled_value
my_object = Cell()
my_object.double_it(2) # will reurn 4

class Cell:
    def add_them(self, x, y): # the self is there to recieve the id of the instance, value will recieve the 2, without self it will crash
        added_value = x + y
        return added_value
my_value = Cell()
my_value.add_them(2, 3) # implicitly, this message will always send the id of the object
Cell.added_value(2, 3) # using the class name does not need the self parameter to execute the method,
                       # and is not consistent with object-oriented programming, which aims to create
                       # instances of classes that can communicate with each other

A Python Instance (of) Method
class Cell:
    def add_them(self, x, y): # the self is there to recieve the id of the instance, value will recieve the 2, without self it will crash
        added_value = x + y # method/behavior
        return added_value
object_1 = Cell()
object_2 = Cell()
object_3 = Cell()
print(object_1.add_them(1, 2)) # instance method
print(object_2.add_them(4, 5))
print(object_3.add_them(33, 67))

Python's Initialization Method, __init__  method
Each object will have:
    it's own variables, e.g self.name, assigned to actual customer names
    its own copy of the class Initialization method:
    an Initialization method, __init__
    its own copy of a get_customer_name method

class CurrentAccount:
    def __init__(self, customer_name): # when you create an instance of a class, this method will be called,
                                       # and it will set up some of the attributes of that instance,
                                       # initialize the attributes of that instance
        self.name = customer_name

    def get_customer_name(self): # the self is there to recieve the id of the instance, value will recieve the 2, without self it will crash
        return self.name

account_holder = CurrentAccount('Rita Jones') # creates the instance of the class
print('the customer name is', account_holder.get_customer_name())

class Human(object): # baby born... 1. Class declared
    def __init__(self, name, gender): # self is the instance itself.. 3. attributes of instance defined
        self.gender = gender
        self.name = name

    def speak_name(self):             # 4. Methods for accessing attributes defined
        print("the baby's name is", )

Able = Human('Atiki', 'Male') # 2. Instance of class

class Rectangle(): # baby born... 1. Class declared
    def __init__(self, width, length): # 3. attributes a rectangle needs to have
        self.width = width # variable to store first attribute of the instance created
        self.length = length # variable to store second attribute of the instance created
                             # an attribute not preceded by self. returns error
# Methods to go with Rectangles:
    def area(self):             # 4. Methods for accessing attributes defined
        return self.width * self.length

    def perimeter(self):             # 4. Methods for accessing attributes defined
        self.width * 2 + self.length * 2

my_rect = Rectangle(5, 6) # 2. Instance of class
another_rect = Rectangle(2, 10)
print(my_rect.area())
print(another_rect.area())
print(my_rect.perimeter())
prinit(another_rect.perimeter())

Local variables in Python Methods
class Cube(): # 1. Class declared
    def __init__(self, width, length, height): # 3. attributes a cube needs to have
        self.width = width # variable to store first attribute of the instance created
        self.length = length # variable to store second attribute of the instance created
        height = 0           # not preceded by self. returns attribute error, because variable is "local" to that method

# Methods to go with Rectangles:
    def volume(self):             # 4. Methods for accessing attributes defined
        return self.width * self.length * self.height # returns attribute error, because variable "height" is "local" to the method __init__

    def perimeter(self):             # 4. Methods for accessing attributes defined
        self.width * 2 + self.length * 2 + self.height * 2

my_volume = Cube(5, 6, 7) # 2. Instance of class
another_volume = Cube(2, 10, 20)
print(my_volume.volume())
print(another_volume.volume())
print(my_volume.perimeter())
prinit(another_volume.perimeter())
