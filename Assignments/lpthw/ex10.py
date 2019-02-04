# Escape Sequences
# Prefixing a special character with "\" turns it into an ordinary character. This is called "escaping".
print('It\'s raining') # "\'" is the single quote character.  # Output: "It's raining".
print("\"hello\"") # Output = "hello"
print('"\\" is the backslash') # Output = "\" is the backslash; "\" used to escape itself

# \t
print("apple\torange")
tabby_cat = "\tI'm tabbed in." # \t = inserts a horizontal Tab
persian_cat = "I'm split\non a line." # \n moves end of sentence to next line
backslash_cat = "I'm \\ a \\ cat." # "\" used to escape itself

# There are a lot of places you’ll see *; below, * is prefixed with "\t" to turn it into a bullet
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
