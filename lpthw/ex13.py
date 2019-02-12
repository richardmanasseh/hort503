# Ex 13: Parameters, Unpacking, Variables
# When you want to run a script on the terminal, sometimes you want to provide additional arguments to it, in order to alter the way the script executes.
# In Exs 11 and 12, we used input() to get the input while the python program / script is running (=interactively)
# Whenever we obtain user information before running the script, we'll hold this user input in a variable called ARGV,...
# ARGV cab then pass them to the script when you run it.
# ARGV is one of the sub-systems in an in-built program called sys
# ARGV holds input as a list, the first member in this list being the script's file name.
# Each item in the list has an assigned index value, designated agrv[0], agrv[1], agrv[2], etc.
# Your script e.g. ex13.py would be stored automatically in argv element 0 (agrv[0]) all the time.
# The next after that e.g. ext13.py test.txt, gets automatically stored in argv[1]
# To use ARGV, we need to first import the sys module.
    # # In general, you import modules because you want to use some functionality from that module.
    # import sys = this says “give me access to all the stuff in the sys module
    # sys.argv[0] = this simply says “get the string that is stored at index 0 in the list sys.argv and do nothing with it”
    # import sys print sys.argv[0] = this says “get the string that is stored at index 0 in the list sys.argv and print it”

# import
# s = sys.argv[0] this says “get the string that is stored at index 0 in the list sys.argv and assign it to the variable s”

# By default when importing, Python will search for modules in
    #(i) a built-in location associated with the Python distribution,
    #(ii) the folder containing the program being executed, and optionally,
    #(iii) any folders included in the $PYTHONPATH environment variable.

from sys import argv

script, first, second, third = argv # this is called unpacking argv; we assign it to each input obtained from the user.
                                    # like saying, 'take whatever is in argv, unpack it, and assign it to all these variables on the left in order'

print(argv[0]) # prints full path to ex13.py
print(argv[1])

# read the WYSS section for how to run this
# This script iterates over the ARGV array and prints out its contents.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# **** Run the program with all three arguments
      # python e13.py first, second, third
