# Ex 8: More Printing & Formatting

formatter = "{} {} {} {}"
# call the ".format()" function to the variable 'formatter':
print(formatter.format(1, 2, 3, 4)) # pass four arguments, which matches with the four {}s in the formatter variable
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) # calling str.format on the variable formatter itself
print(formatter.format(
     "World",
     "Africa",
     "Eastern Africa",
     "Uganda"
))
