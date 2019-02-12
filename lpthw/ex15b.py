# Reading Files
# Python has a built-in function open() to open a file.
# The syntax to open a file object in Python is: file_object  = open(“filename”, “mode”)
    # generally we want to store this open file inside of a variable aka a file handle, here file_object
# We can specify the mode while opening a file:
    # to read (default)'r'' open("test.txt", "r")
    # to write 'w': open("test.txt", "w")
    # .append to add 'a' to the file.
    # 'r+' to open a file for updating (both reading and writing)

# PS C:\Users\rmann\lpthw> python ex15.py ex15.txt
from sys import argv

script, filename = argv # filename = index variable for ex15.txt, or other file you want program to read
                        # script = index variable for ex15.py
# argv[1] # full path to ex15.txt

txt = open(filename) # open() function, just like print() function

print(f"Here's your file {filename}:")
print(txt.read()) # returns the entire file

txt.close()
