"""
The pass statement in Python is a null operation — 
it does nothing when executed. It is used as a placeholder when a statement is syntactically required, 
but you don't want to execute any code. 
"""

x = 10

if x > 5:
    pass  # Do nothing if the condition is true
else:
    print("x is 5 or less")

# The program doesn't do anything for the "if" condition but executes the "else" branch.
