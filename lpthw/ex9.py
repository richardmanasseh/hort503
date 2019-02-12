# Ex 9: More Printing.

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun" # prints list on a continuous lineself.

# Line continuation is automatic when the split comes while a statement is inside parenthesis ( ( ), brackets ( [ ) or braces ( { ).
# indicate that the statement that was started on line 1 is continued on line 2

# \n breaks the string print into separate lines:
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #the line continuation character (\) alone would denote a normal backslash (\).
                                                    # \n is equivalent to Enter key
print("Here are the days:", days)
print("Here are the months:", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
# A string is read the way it is (=literally): text. Hence the term "string literals".
# That means you can misspell it, fill it with weird words, and even fill it with weird, misspelled words.
# You still won’t get an error message from Python.
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
