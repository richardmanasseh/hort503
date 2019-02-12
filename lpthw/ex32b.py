# Error Handling

try: # try a block of code...and if there's an exception, it's gonna do something else
    12/0
    print(answer)
except: # exception = error
    print("An error occured") # Custom error, rather than the more comprehensive python traceback
    print("sorry. error!")    # # Sorry, this file doesnot exist.
# Output: "An error occured"
          # this is because when the program tries to execute the statement answer 21/0 in the try block,
          # an error occurs since you cannot divide a number by zero
          # so the remaining try block is ignored and the statement in the except block is executed instead
