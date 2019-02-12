# Ex 12: # Example 2: How input() works in Python?:
# input has an optional parameter, which is the prompt string.
# In this case, "How old are you?", is written as an optional parameter, and will be printed on the screen.

# Algorithm:
# Step 1 Define your problem as in ex 11).
# Step 2 Algorithms input(s): # prompts (questions)
                              # user responses/entries
# Step 3  Define the algorithm's (input and output) variables: user responses/entries
# Step 4 Outline the algorithm's operation(s): # print prompts # call print() function
                                               # input user response # call input() function for accepting data directly from the user
                                               # press Enter
# Step 5 Output the results (output) of your algorithm's operations: input from the user, files, displayed on the screen, console (as a STRING).

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input(f"Wow {height}? Great! How much to you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
