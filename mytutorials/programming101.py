# Basic Programming
    #>>Python Program Design
    Input Information   >>>>|>> DATA                     DATA  >>| Output Information                                             Information
        Age                 |  input >>>> process >>>>   output  |  Graph/pie chart showing
        Gender              |                                    |  how many are in each category

A computer has no notion of information: it doesn't understand what's age, gender; has no idea of
who is male or female; it cannot see the graph that's being produced.
A cmputer programmer has the responsibility of taking the Input Information and converting it into
the form that a computer will understand, and that's DATA.
The computer system will then work on this data to produce output data, which will then be converted
into a form that a human can understand, that is, Output Information

So a computer programmer has to think how to represent Input Information in a Data Format
Whatever the format, the programmer will now have to process this Input Data to produce an
output, i.e. Output Data.

When data is supplied as an imput to the computer, it has to be stored somewhere in the
computer's memory locations. We then process this data, and the results will also be stored
in the computer's memory locations.

We store data in things called programme variables. A Program Variable is a Named Area of
computer's memory. We're not so much concerned as to where the area is, all we are concerned
is the fact that we can give it a Sensible Name.

The process in the middle of the input and output data is a pile of Program Statements or
instructions for manipulating the data; taking the Input Data (stored in program variables),
processing it in someway to produce the result called Output Data (then also stored
in program variables).

A programmer is responsible for deciding what the data will be, what the variables are,
as well as the program statements that will manipulate the data stored in those variables.
>> PROGRAM = Program Statements + Program Variables

Case: Develop a program that calculates an individual's grosspay
In order to write a program that tells the computer to perform/do this task, you youself have got to
understand how to perform the task (the problem)..
...so you'll just be telling the computer to carry out the task on your behalf.

Grosspay equals hourly rate times the number of hours worked
    Example:
        hourly payrate = $10 per hour
        number of hours worked = 35 hours

        As a computer programmer we need to decide:
            > what the data is
            > what program variables are needed to store this data
            > what program statements are needed to maniplate the data stored in the program variables

        Data Table:
        Variable Name           Type                Comment
        hourly_pay_rate      Number(float)       Used to store the pay rate input
                                                and used in the calculation
        hours_worked        Number(float)       Used to store the hours worked input
                                                and used in the calculation
        gross_pay           Number(float)       Used to store the calculated gross pay

        We produce an Algorithm to decide what our program statements need to be.
        Here, the algorithm has four steps:
            > obtain hourly rate of pay (for this program, user is going to type it in with keyboard) # INPUT
            > obtain number of hours worked (user input still) # INPUT
            > calculate the gross pay # PROCESS
            > display the gross pay # OUTPUT

        This gives the following program:
            DATA INPUT          >>>>        PROCESS                 >>>>      DATA OUTPUT
            hourly_pay_rate             calculate the gross pay                 gross_pay
            hours_worked

        Coding the Program Design to a Python Program:
        # obtain hourly rate of pay # user INPUT
        hourly_pay_rate = float(input('please enter the rate of pay per hour: '))
                        # 7.2 would first be converted to its binary code and
                        # stored as a std input file in a temporary memory called a buffer
                        # next, stage is to convert what's stored in the buffer into a float
                        # using the float part of this statement..
                        # this float is then stored in the hourly_pay_rate variable
        # obtain number of hours worked # user INPUT
        hours_worked = float(input('please enter the hours worked: '))
                        # 35 would first be converted to its binary code and
                        # stored as a std input file in a temporary memory called a buffer
                        # next, stage is to convert what's stored in the buffer into a float 35.0
                        # using the float part of this statement..
                        # this float 35.0 is then stored in the hours_worked variable

        # calculate the gross pay # PROCESS
        gross_pay = hourly_pay_rate * hours_worked # read, product of what's stored in hours_worked
                                                   # and hourly_pay_rate
                                                   # the computer hardware will now be responsible
                                                   # for transfering a copy from these variables to ALU
                                                   # which will multply them to give 252.0 that will now
                                                   # be assigned to gross_pay
        # display the gross pay # OUTPUT
        print('The gross pay is $' + str(gross_pay))
            # we pass what's stored in gross_pay to the str to give us the string representation of gross_pay
            # we then join this with the string'The gross pay is $' (aka concatenation)
            # we now have a fully formed string which goes to the Visual Display Unit to be displayed
