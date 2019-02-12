# Memorizing Logic
Logic on a computer is all about determining if something is True or False at a specific instance (point) in the program
Usually you have two variables say A and B,
There are three logical operators that are used to compare values.
They evaluate expressions down to Boolean values, returning either True or False.
These operators are and, or, and not and are defined in the table below.
    and     = True if both are true
    or      = True if at least one is true
    and not = True only if false

To understand how logical operators work, let’s evaluate three expressions:

print((9 > 7) and (2 < 4))  # Both original expressions are True # Output: True
                            #both 9 > 7 and 2 < 4 needed to evaluate to True
print((8 == 8) or (6 != 6)) # One original expression is True    # Outpt: True
                            # since 8 == 8 evaluated to True, it did not make a difference that 6 != 6 evaluates to False because the or operator was used.
                            If we had used the and operator, this would evaluate to False.

print(not(3 <= 1))          # The original expression is False
                            # the not operator negates the False value that 3 <=1 returns.
