# Python Strings and String Formatters in Python 3
# Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0
# with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

# The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator.

# Overall comment: 4 places with strings (") or (')  in here
types_of_people = 10
# a string
x = f"There are {types_of_people} types of people." # letter f for ”format” is added alert python of variable insert

binary = "binary"
do_not = "don't"
# a second string
y = f"Those who know {binary} and those who {do_not}." # letter f for ”format” is added alert python of variable insert

print(x)
print(y)

# third set of strings
print(f"I said: '{x}'") # '{x}' inserts variable in quotes
print(f"I also said: '{y}'")

# Formatters work by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {} — into a string and calling the str.format() method.
# You’ll pass into the method the value you want to concatenate with the string.
# This value will be passed through in the same place that your placeholder is positioned when you run the program.

#Ex 1 we've a string with a pair of curly braces as a placeholder:

print("Sammy has {} balloons.".format(5)) # We added str.format() method and passed the value of the integer 5 to that method.

# Ex 2 We can also assign a variable to be equal to the value of a string that has formatter placeholders:

open_string = "Sammy loves {}."
print(open_string.format("open source"))

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" # {} is a formatter placeholder for a value that you intend to pass through with the str.format() method.

print(joke_evaluation.format(hilarious))

# 4th string
w = "This is the left side of..."
e = "a string with the right side."

print(w + e) # for strings, the operator + represents concatenation
