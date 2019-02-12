Python in-built Functions
abs(x): returns the absolute value of an integer, floating point, or complex number.
    >>> abs(3.14), 3.14; >>> abs(-3.14), 3.14; >>> abs(3+4j), 5.0
all(): returns True if all elements of the supplied iterable are true
    >>> lst = [1, 2, 3, 4, 5, 6]
    >>> all(lst)
    True

any(): the converse of the all() function. any() returns True if any element of the iterable evaluates true.

1. True : This keyword is used to represent a boolean true. If a statement is truth, “True” is printed.
2. False : This keyword is used to represent a boolean false. If a statement is False, “False” is printed.
True and False in python are same as 1 and 0.Example:

3. None : This is a special constant used to denote a null value or a void. Its important to remember, 0, any empty container(e.g empty list) do not compute to None.
It is an object of its own datatype – NoneType. It is not possible to create multiple None objects and can assign it to variables.

4. and : This a logical operator in python. “and” returns true if both the operands are true. Else returns false.The truth table for “and” is depicted below.
5. or : This a logical operator in python. “or” returns true if any one of the operand is true. Else returns false.The truth table for “or” is depicted below.
6. not : This logical operator inverts the truth value.The truth table for “not” is depicted below.
7. assert : This function is used for debugging purposes. Usually used to check the correctness of code. If a statement evaluated to true, nothing happens, but when it is false, “AssertionError” is raised . One can also print a message with the error, separated by a comma.
8. break : “break” is used to control the flow of loop. The statement is used to break out of loop and passes the control to the statement following immediately after loop.
9. continue : “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop, but does not end the loop.

10. class : This keyword is used to declare user defined classes.For more info. click here.
11. def : This keyword is used to declare user defined functions.For more info. click here.
12. if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.
13. else : It is a control statement for decision making. False expression forces control to go in “else” statement block.
14. elif : It is a control statement for decision making. It is short for “else if”
if, else and elif conditional statements are explained in detail here article.
15. del : del is used to delete a reference to an object. Any variable or list value can be deleted using del.

16. try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.
17. except : As explained above, this works together with “try” to catch exceptions.
18. raise : Also used for exception handling to explicitly raise exceptions.
19. finally : No matter what is result of the “try” block, block termed “finally” is always executed.

20. for : This keyword is used to control flow and for looping.
21. while : Has a similar working like “for” , used to control flow and for looping.
22. pass : It is the null statement in python. Nothing happens when this is encountered. This is used to prevent indentation errors and used as a placeholder

23. import : This statement is used to include a particular module into current program.
24. from : Generally used with import, from is used to import particular functionality from the module imported.
25. as : This keyword is used to create the alias for the module imported. i.e giving a new name to the imported module.. E.g import math as mymath.
26. lambda : This keyword is used to make inline returning functions with no statements allowed internally.
27. return : This keyword is used to return from the function.

28. yield : This keyword is used like return statement but is used to return a generator. Detailed Article – yield keyword
29. with : This keyword is used to wrap the execution of block of code within methods defined by context manager.This keyword is not used much in day to day programming.
30. in : This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.
31. is : This keyword is used to test object identity, i.e to check if both the objects take same memory location or not.

32. global : This keyword is used to define a variable inside the function to be of a global scope.
33. non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.
