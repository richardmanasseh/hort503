# Reading Files
# Python has a built-in function open() to open a file.
# The syntax to open a file object in Python is: file_object  = open(“filename”, “mode”)
    # generally we want to store this open file inside of a variable aka a file handle, here file_object
# We can specify the mode while opening a file:
    # to read (default)'r'' open("test.txt", "r")
    # to write 'w': open("test.txt", "w")
    # .append to add 'a' to the file.
    # 'r+' to open a file for updating (both reading and writing)

# Algorithm:
# Step 1 Define your problem: read a textfile.
# Step 2 Algorithms input(s): name of your textfile
                            #
# Step 3  Define the algorithm's (input and output) variables: script, filename, argv
                                                              # file = open(filename), file = file handle
# Step 4 Outline the algorithm's operation(s): open the file # call the open(filename)
                                             # print it using the read() command as, print file.read()
# Step 5 Output the results (output) of your algorithm's operations:  display contents of file

# Run the program, passing the name of the text file to be printed as an argument, like this PS C:\Users\rmann\lpthw> python ex15.py ex15.txt

from sys import argv

script, filename = argv # since one file to read, we will pass two arguments – the script name (argv[0]) and the filename
                        # filename = index variable for ex15.txt, or other file you want program to read
                        # script = index variable for ex15.py
# argv[1] # full path to ex15.txt

txt = open(filename) # open() function, just like print() function

print(f"Here's your file {filename}:")
print(txt.read()) # returns the entire file

print("Type the filename again:")
file_again = input("> ")           # ex15.txt

txt_again = open(file_again)

print(txt_again.read())
