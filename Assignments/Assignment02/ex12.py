# A repeat of ex11, but with the input prompt specified directly
# Since input is a function that returns a result (the string we got from the user), we can use variable assignment like we learned in the previous chapter to capture the response.
# Adding variable assignment gives Python a convenient place to hold the value.
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input(f"Wow {height}? Great! How much to you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
