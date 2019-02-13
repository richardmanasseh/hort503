# Asking questions in Python
# We'd like to pose a question, give a prompt, and wait for the user to enter in the answer.
# There is a built-in function called input that does exactly this.
# Since input is a function that returns a result (the string we got from the user), we can use variable assignment like we learned in the previous chapter to capture the response.
# Adding variable assignment gives Python a convenient place to hold the value.

# Syntax for the input() function is input(prompt), where prompt is a string, representing a default message (question) before the input.
# Therefore, this is similar to when you used the () to do a format with extra variables, as in f"{} {}"
print("How old are you?", end=' ') # end= ' ' leaves little space after qn mark so question doesnt go to line 2

age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much to you weigh?", end= ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print(f"At {age}, you are still young.")


print("where are you going?", end= ' ')
city = input()
print(f"safe journey to {city}.")
