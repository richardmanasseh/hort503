# Ex 20: How Functions and Files Work Together:

from sys import argv

script, input_file = argv # input_file run with python script e.g. ex15.txt (file must be in working directory)
                        # on the terminal, to be run as python ex20.py ex15.txt

# Define a function called print_all, with parameter f, for "file" # "f" is very common to mean a file object.
def print_all(f):
    print(f.read())
    # After the whole file is read the cursor is at the end of file.

# Define another function called rewind which accepts a file as parameter
def rewind(f):
    f.seek(0) # This seek method will bring the cursor to the position mentioned inside the parantheses.
              # In n this case, it is seek(0) this will bring you to the beginning (first byte) of the file because 0 is specified.
              # f.seek(2): brings you back to the third byte/ (letter after start e.g from "Mary" to "ry") of the file

# Define yet another function called print_a_line, which accepts two parameters: line_count and file
def print_a_line(line_count, f):
    print(line_count, f.readline()) # f.readline() method to an open reads a single line from the file
                                        # .readlines() produces a list of all the lines in the file i.e.
                                        # returns the list ['Line 1\n', 'Line 2\n', Line 3\n']
                                        # where each line still ends in the newline character '\r\n' in Windows.
                                        # the .read() method to an open file: it produces one giant string..
                                            # that contains all the lines in the file, each ended by the newline character '\n'.
                                            # calling open_file.read() returns the string 'Line 1\nLine 2\nLine 3\n'
# Open a file
current_file = open(input_file) # input_file (ex20.txt)

print("First let's print the whole file:\n") # Print "First let's print the whole file:"

print_all(current_file) # call the print_all function to print the whole file ex15.txt

print("Now let's rewind, kind of like a tape.") # Print "Now let's rewind, kind of like a tape."

rewind(current_file) # Call the rewind function to go back to the beginning of the file

# Now print three lines from the top of the file

# Print "Let's print three lines:"
print("Let's print three lines:")

# Set current line to 1
current_line = 1 # Now since we are at the beginning of the file.i.e line 1 we set the variable current_line = 1 and then called the function which...
                # will print a single line.
print_a_line(current_line, current_file) # Print current line by calling print_a_line function

current_line = current_line + 1 # Set current line to 2 (second line) by adding 1
# current_line = current_line + 1 is equivalent to current_line += 1: += adds another value with the variable's value and assigns the new value to the variable.
print_a_line(current_line, current_file) # Print current line by calling print_a_line function

# Set current line to 3 by adding 1
current_line = current_line + 1 # vs short-hand notation: "current_line += 1"
print_a_line(current_line, current_file) # Print current line by calling print_a_line function
