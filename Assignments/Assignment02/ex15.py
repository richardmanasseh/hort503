#Reading Files
# Python has a built-in function open() to open a file.
# We can specify the mode while opening a file: to read (default)'r', write 'w' or append 'a' to the file.
# 'r+' to open a file for updating (reading and writing)

from sys import argv

script, filename = argv # text2.txt is file you waant to read

txt = open(filename) # open() function, just like print() function
# generally we want to store this open file inside of a variable aka a file handle, here called txt
print(f"Here's your file {filename}:")
print(txt.read()) # returns the entire file

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
