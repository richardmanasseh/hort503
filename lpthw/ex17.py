# Copying One File to Another

from sys import argv
from os.path import exists # Also required: "exists" command frrom sub-module os.path of the os module; returns "True" a file exists.
                           # The os and sys modules provide numerous tools to deal with filenames, paths, directories.

# Algorithm:
# Step 1 Define your problem: Copying One File to Another
# Step 2 Algorithms input(s): argv, exists (in-built)
                            # script, from_file, to_file
# Step 3  Define the algorithm's (input and output) variables: script, filename, argv, file handle(s)
                                                              # file = open(filename), file = file handle
# Step 4 Outline the algorithm's operation(s): open the from_file into a file handle # call the open(filename)
                                             # read() the from_file into a file handle, print file.read()
                                             # open destination file to_file (also into a file handle)
                                             # now write into destination file
                                             # close opening file handles
# Step 5 Output the results (output) of your algorithm's operations: copy of from_file (e.g. ex17.txt) created as to_file (ex17b.txt)

# Run the program, passing the name of the text file to be printed as an argument, like this PS C:\Users\rmann\lpthw> python ex15.py ex15.txt ex15b.txt


script, from_file, to_file = argv # from_file = ex17.txt, to_file = ex17b.txt
# PS C:\Users\rmann\lpthw> python ex17.py ex17.txt ex17b.txt
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') # open destination file
out_file.write(indata) # now write into destination file

print("Alright, all done.")

out_file.close()
in_file.close()
