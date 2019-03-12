# Ex 38: Doing Things to Lists
# Most variables have a single value in them:
    # x = 2, ... and when we put a new value in the variable, say,
    # x = 4,...the old value is overwritten, so calling x returns 4
# Lists are a way to assign a variable many values
# Lists are enclosed in square brackets ( [ and ] ):
my _x_values = [2, 4]
# Elements in a list are indexed from 0
# An element can  be accessed using it's index:
print(my_x_values[0]) # returns 2

# we can change the elements in a list:
my _x_values[0] = 3
print(my_x_values) # returns [3, 4]

# the len() function takes a list as parameter and returns the number of elements in it
# in general, the len() function returns the number of elements in any set, including a string
print(len(my_x_values)) # should return 2

# you can generate a list using the range function:
my_list = range(4) # returns a list of numbers that range from 0 upto but not including the parameter

# we can combine the range() and len() functions to create a numerical list from a string
my_friends = ['john', 'james', 'david','dan']
my_friends_list = range(len(my_friends) # returns [0, 1, 2, 3]

# these two loops are then equivalent:
for friend in my_friends:
    print("happy new year", friend)

for i in range(len(my_friends):
    friend = my_friends(i) # go through my_friends and
    print("happy new year", friend)

# we can concatenate lists just as we can concatenate strings with +
a = [1,2]
b = [3,4]
c = a + b
print(c) # [1,2,3,4]

# Lists can be sliced (reverse of concatenation):
c = [1,2,3,4]
c[1:3] # slices from index 1 to but not including index 3, returns [2,3]
c[:3] # slices (from index 0) upto but not including index 3, so returns [1,2,3]
c[3:] # slices (from index 3) upto the end, so returns [4]
c[:] # same as c

# python provides two logical operators that help you check if something is in a list
# they are "in" and "not in" # returning True or False
 5 in c # is 5 in c?
 5 not in c

# there are many functions in python that take lists as parameters
my_friends.sort() # sorts the list in alphabetical order
print(len(c))
prin(sum(c))
print(min(c))
print(max(c))
print(sum(c)/len(c)) # average

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# we can pass a string to split(), which will return a list
stuff = ten_things.split(' ') # string.split("delimiter")
                              # e.g. mary = 'Mary had a little lamb'
                              # => mary.split() >>> ['Mary', 'had', 'a', 'little', 'lamb']
                              # default delimiter is space between elements in a string
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: #
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!


# Popping three elements and printing them
S = {1, 2, 3, 4, 5}
print(S.pop())
print(S.pop())
print(S.pop())

# The updated set
print("Updated set is", S)

# Python program to demonstrate the # use of join function to join list
# elements with a character.

list1 = ['1','2','3','4']

s = "-"

# joins elements of list1 by '-'
# and stores in string s
s = s.join(list1)

# join use to join a list of
# strings to a separator s
print(s)
