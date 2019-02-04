# Here's some new strange stuff, remember type it exactly.

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun" # prints list on a continuous lineself.

# Line continuation is automatic when the split comes while a statement is inside parenthesis ( ( ), brackets ( [ ) or braces ( { ). This is convenient, but can also lead to errors if there is no closing Parenthesis, bracket or brace.
# indicate that the statement that was started on line 1 is continued on line 2

# \n breaks the string print into separate lines:
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #the line continuation character (\) only would denote that the backslash (\) to indicate that a statement is continued on the next line..

print("Here are the days:", days)
print("Here are the months:", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
#
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
