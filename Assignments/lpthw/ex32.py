# Loops and Lists
# To keep a computer doing useful work we need repetition, looping back over the same block of code again and again.
# Here's how you make lists: in []
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# Python programming language provides following types of loops to handle looping requirements: For Loops, While Loops, and Nested Loops
# The For-Loop that is used to iterate over elements of a sequenceself.
# It is often used when you have a piece of code which you want to repeat "n" number of time.
# So For-Loop works like this: " for all elements in a list, do this "

# this first kind of for-loop goes through a list
for number in the_count: # That reads, for every number in the variable "the_count"
    print(f"This is count {number}")

# same as above
for fruit in fruits:# for the variable fruit, iterate through all the elements in the list "fruits"
    print(f"A fruit of type: {fruit}") # fruit is a new variable that holds the current fruit type

# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = [] # instantiates a new list object

# then use the range function to do 0 to 5 counts
for i in range(0, 6): # without the range function, i=1 and i=6
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i) # Use append() to add to elements

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

alphabet = ['a', 'b', 'c']
alphabet.append('d')
print(alphabet)
