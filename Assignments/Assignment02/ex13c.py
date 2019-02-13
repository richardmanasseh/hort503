# Another way to pass variables to a script

from math import pi # module math is not imported, rather just pi has been imported as a variable.

# Note that in the above example,
# we used math.pi. Here we have used
# pi directly.
print(pi) # Output = 3.141592653589793

from math import * # All the functions and constants can be imported using *
print(pi)
print(factorial(6))
# Output: 3.141592653589793
#         720
