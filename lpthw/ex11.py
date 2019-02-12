# Asking Questions in Python
# Challenge: We'd like to pose a question, give a prompt, and wait for the user to enter in the answer.
# There is a built-in function called input that does exactly this.
    # if the input function is called, a script's flow will be stopped until the user has given an input and has ended the input with the Enter key.
    # The input() method is used to ask the user of the program (not the programmer) a question, and then wait for a typed response.
# Assigning a variable to input gives Python a convenient place to hold the value.

# Syntax for the input() function is input(prompt)
# Prompt is the visual cue that tells the user that the system is ready to accept input data.

# Example 1: How input() works in Python?
# Algorithm:
# Step 1 Define your problem (above).
# Step 2 Algorithms input(s): prompts (questions)
                            # user responses/entries
# Step 3  Define the algorithm's (input and output) variables: user responses/entries
# Step 4 Outline the algorithm's operation(s): # print prompts # call print() function
                                               # input user response # call input() function for accepting data directly from the user
                                               # press Enter
# Step 5 Output the results (output) of your algorithm's operations: input from the user, files, displayed on the screen, console (as a STRING).


print("How old are you?", end=' ') # end= ' ' so answer is entered on same line as question.
age = input("> ") # e.g. >>> is called the Python prompt. "> " is an optional parameter, i.e. the prompt, and will be printed on the screen.
print("How tall are you?", end= ' ')
height = input()
print("How much to you weigh?", end= ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print(f"At {age}, you are still young.")

print("where are you going?", end= ' ')
city = input()
print(f"safe journey to {city}.")
