# While-Loops
# The while loop tells the computer to do something as long as the condition is met
# it's construct consists of a block of code and a condition.

# It works like this: " while this is true, do this "

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
