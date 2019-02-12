# While-Loops
# The while loop tells the computer to do something as long as the condition is met
# it's construct consists of a block of code and a condition.

# It works like this: " while this is true, do this "

i = 1 # intially i =1

while i <= 10: # loop condition, interpreter first checks if this condtion is true

    print(i) # 1 < 10, prints 1
    i = i + 1 # then adds 1 to i, so i now goes from 1 to 2 (i+=1), overwiting the intital value of 1
              # program then goes back to check the loop condition once more, and executes the code inside the loop again
              # loop is evaluated for values of i in the range 1-10
print("Done with loop")

# Output: list, 1-10

x = 5

while x > 0:
    print(f"timeleft = ", x)
    x -= 1 # decreases the value of munutes by 1, then assigns this new value back to minutes, overwiting the intital value of 5
                 # we need to decrease the value of minutes by 1 so that the loop condition while minutes > 0 will eventually evaluate to false
                 #If we forget that, the loop will keep running endlessly resulting in an infinite loop
                 # ...in this case the program would keep printing timeleft = 5 until you somehow kill the program

z = 1 # intially z =1

while z <= 15: # loop condition, interpreter first checks if this condtion is true
    if z == 12:
        break   # break statement to prematurely terminate the excecution of the loop
    else:
        print(z) # 1 < 15, prints 1
    z = z + 1
# Output: list, 1-11
