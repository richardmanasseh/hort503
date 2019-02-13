# While-Loops
# The while loop tells the computer to do something as long as the condition is met
# it's construct consists of a block of code and a condition.

# It works like this: " while this is true, do this "

b = 6
numbers = []
def while_func(b):
    i = 0
    while i < b:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

def print_results(nums):
    print("The numbers: ")
    for num in nums:
        print(num)

print_results( while_func(6) )
print_results( while_func(5) )
