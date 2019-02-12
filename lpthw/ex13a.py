# Ex 13: Parameters, Unpacking, Variables

from sys import argv

script, age, height, weight, hello, world = argv # this is called unpacking argv; we assign it to each input obtained from the user.
                                    # like saying, 'take whatever is in argv, unpack it, and assign it to all these variables on the left in order'

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print(f"At {age}, you are still young.")

for x in argv:
     print("Argument: ", x)
