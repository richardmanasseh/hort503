# More Printing & Formatting
print("Mary had a little lamp.")
print("Its fleece was white as {}. ".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # Prints string (".") ten times

# By default python’s print() function ends with a newline, because it comes with a parameter called ‘end’.
# By default, the value of this parameter is ‘\n’, i.e. the new line character.
# Line ending uses Windows convention of "\r\n" .

print("Welcome to" , end = ' ')
print("GeeksforGeeks", end = ' ') # Output: Welcome to GeeksforGeeks

print("Python" , end = '@')
print("GeeksforGeeks")  # Python@GeeksforGeeks

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it and see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end= ' ')
print(end7 + end8 + end9 +end10 + end11 + end12)
