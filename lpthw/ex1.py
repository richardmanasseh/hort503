
Algorithm and flowchart are the powerful tools for learning programming.
An algorithm is a step-by-step analysis of the process, while a flowchart explains the steps of a program in a graphical way.
Algorithm and flowcharts helps to clarify all the steps for solving the problem.
For beginners, it is always recommended to first write algorithm and draw flowchart for solving a problem and then only write the program.

HOW TO WRITE ALGORITHMS
Step 1 Define your problem e.g.
        to calculate the area of rectangle
        given a list of positive numbers, return the largest number on the list.
Step 2 Define your algorithm's input(s) or input parameters:  many algorithms TAKE IN data, e.g. to calculate the area of rectangle input may be the rectangle length and width.
Step 3 Define the variables: varaibles hold an algorithm's data. 
            We can define two variables for rectangle length and rectangle width as LENGTH and WIDTH.
            Always use meaningful variable names e.g. LENGTH, WIDTH not L & W.
            AREA
        
Step 4 Outline the algorithm's operations: e.g. 
                                                multiply the HEIGHT and WIDTH variable and store the value in new variable (say), AREA.
                                                    AREA = HEIGHT * WIDTH
                                                multiply the LENGTH and WIDTH variable and store the value in new variable (say) AREA.
                                                then multiply the AREA and HEIGHT variable and store the value in new variable VOLUME.
                                                    AREA = LENGTH * WIDTH
                                                    VOLUME = AREA * HEIGHT
                                                    
                                                    
Step 5 Output the results of your algorithm's operations:  In case of area of rectangle output will be the value stored in variable AREA.
       If the input variables described a rectangle  with a HEIGHT of 2 and a WIDTH of 3, the algorithm would return/output the value of 6.

Algorithm¶ Example 1
Consider a very simple algorithm called find_max().
Problem: Given a list of positive numbers, return the largest number on the list.
Inputs: A list L of positive numbers. This list must contain at least one number.
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

Algorithm¶ Example 2
Name of algorithm: calc_pay.
Problem: we want to calculate and display the net pay and name of every employee in a company.
Inputs: Employee data
Outputs: A number n, which will be the largest number of the list.

Algorithm: Top Level design/Gross Steps Involved
1.	for each employee:
2.	obtain employee record e.g from a file, etc.
3.	calculate pay, which will involve:
4.  Print the wage slip

Algorithm: Refinement of each step/stepwise refinement of each step
1.	for each employee:
2.	obtain/get employee record e.g from a file, etc.
3.	calculate pay, which will involve:
    3.1 calculate the gross pay
    3.2 calculate the deductions
    3.3 calculate the net pay
4. Print the wage slip