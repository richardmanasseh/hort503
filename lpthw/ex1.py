
Algorithm and flowchart are the powerful tools for learning programming.
An algorithm is a step-by-step analysis of the process, while a flowchart explains the steps of a program in a graphical way.
Algorithm and flowcharts helps to clarify all the steps for solving the problem.
For beginners, it is always recommended to first write algorithm and draw flowchart for solving a problem and then only write the program.

HOW TO WRITE ALGORITHMS
Step 1 Define your problem e.g.
        to calculate the area of rectangle
        given a list of positive numbers, return the largest number on the list.
Step 2 Define your algorithms input:  Many algorithms take in data to be processed, e.g. to calculate the area of rectangle input may be the rectangle height and rectangle width.
Step 3  Define the variables:  Algorithm's variables allow you to use it for more than one place.
        We can define two variables for rectangle height and rectangle width as HEIGHT and WIDTH (or H & W).
        We should use meaningful variable name e.g. instead of using H & W use HEIGHT and WIDTH as variable name.
Step 4 Outline the algorithm's operations:  Use input variable for computation purpose, e.g. to find area of rectangle multiply the HEIGHT and WIDTH variable and store the value in new variable (say) AREA.
        An algorithm's operations can take the form of multiple steps and even branch, depending on the value of the input variables.
Step 5 Output the results of your algorithm's operations:  In case of area of rectangle output will be the value stored in variable AREA.
       If the input variables described a rectangle  with a HEIGHT of 2 and a WIDTH of 3, the algorithm would output the value of 6.

An Example Algorithm¶
Let’s look at a very simple algorithm called find_max().
Problem: Given a list of positive numbers, return the largest number on the list.
Inputs: A list L of positive numbers. This list must contain at least one number. (Asking for the largest number in a list of no numbers is not a meaningful question.)
Outputs: A number n, which will be the largest number of the list.

Algorithm:
1.	Set max to 0.  (Initialize our max as 0).
2.	For each number x in the list L, compare it to max. If x is larger, set max to x.
3.	max is now set to the largest number in the list.
An implementation in Python:
def find_max (L):
    max = 0
    for x in L:
        if x > max:
            max = x
    return max
Does this meet the criteria for being an algorithm?

An Example Algorithm¶
Let’s look at a very simple algorithm called find_max().
Problem: Given a list of positive numbers, return the largest number on the list.
Inputs: A list L of positive numbers. This list must contain at least one number. (Asking for the largest number in a list of no numbers is not a meaningful question.)
Outputs: A number n, which will be the largest number of the list.
Initialize our running total (total) as 0.
Algorithm:
1.	Set max to 0.  (Initialize our max as 0.
2.	For each number x in the list L, compare it to max. If x is larger, set max to x.
3.	max is now set to the largest number in the list.
An implementation in Python:
def find_max (L):
    max = 0
    for x in L:
        if x > max:
            max = x
    return max

Does this meet the criteria for being an algorithm?
