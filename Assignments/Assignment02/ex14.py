# Prompt people for information from both the commandline by passing the command line options into your script, or prompting them with the regular input() style
# then you're going to pass that information to print strings
from sys import argv

script, user_name = argv
prompt = '> '
# user_name = rmann in PS C:\Users\rmann>
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you leave {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
