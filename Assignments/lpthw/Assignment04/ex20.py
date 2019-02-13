# Functions and Files:
# Import argv variables from the sys module
from sys import argv
# Assign the first and the second arguments to the two variables:
script, input_file = argv # input_file is file you'll run with this script e.g. ex15.txt (file must be in working directory)
                        # on the terminal, to be run as python ex20.py ex15.txt (tell python to use script ex20.py to process file ex15.py)
# Define a function called print_all, with parameter f, for "file"
def print_all(f):
    print(f.read()) # print the content of the file ex15.txt

# Define another function called rewind to make the file reader go back to different positions of the file
def rewind(f):
    f.seek(0) # make the file reader go back to the first byte (start, 0) of the file
              # f.seek(2): file reader would go back to the third byte/ (letter after start e.g from "Mary" to "ry") of the file

# Define yet another function called print_a_line, with an integer counter and a file object as formal parameters
def print_a_line(line_count, f):
        print(line_count, f.readline()) # line_count prints the line number, f.readline(), the contents of a line
            # the .readlines() method to an open file produces a list of all the lines in the file
            # where each line still ends in the newline character '\r\n' in Windows.

# Open a file
current_file = open(input_file) # From "python ex20.py ex15.txt", script (=ex20.py), input_file (ex15.txt) = argv

print("First let's print the whole file:\n") # Print "First let's print the whole file:"

print_all(current_file) # call the print_all function to print the whole file ex15.txt

print("Now let's rewind, kind of like a tape.") # Print "Now let's rewind, kind of like a tape."

rewind(current_file) # Call the rewind function to go back to the beginning of the file

# Now print three lines from the top of the file

# Print "Let's print three lines:"
print("Let's print three lines:")

# Set current line to 1
current_line = 1 # first line
print_a_line(current_line, current_file) # Print current line by calling print_a_line function

current_line = current_line + 1 # Set current line to 2 (second line) by adding 1
# current_line = current_line + 1 is equivalent to current_line += 1: += adds another value with the variable's value and assigns the new value to the variable.

print_a_line(current_line, current_file) # Print current line by calling print_a_line function

# Set current line to 3 by adding 1
current_line = current_line += 1 # vs short-hand notation: "current_line += 1"

print_a_line(current_line, current_file) # Print current line by calling print_a_line function
