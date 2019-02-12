# Ex 38: Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # string.split("delimiter") e.g. mary = 'Mary had a little lamb' => >>> mary.split() >>> ['Mary', 'had', 'a', 'little', 'lamb']
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # len() returns the length of list.
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
