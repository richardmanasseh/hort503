from sys import argv

script, first, second, third = argv

# module sys is not imported, rather just argv has been imported as a variable.
# Python modules can get access to code from another module by importing the file/function using import

# sys = system library, contains some of the commands one needs in order to work with command-line arguments
# argv is aka argument vector,
# Arguments are command modifiers that change the behavior of a command.
# read the WYSS section for how to run this

# whenever you run a script e.g. ex13.py on the command-line, s soon as you hit Enter, that program gets stored automatically in argv element 0 (agrv[0]) all the time
# if you put any thing else after that e.g. ext13.py test.txt, it will automatically get stored in argv[1]

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# **** Run the program with all three arguments
