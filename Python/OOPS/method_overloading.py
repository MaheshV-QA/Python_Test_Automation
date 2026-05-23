"""
Polymorphism:
-------------
==> One thing showing multiple behaviour is called as polymorphism.

1. Compile time polymorphism :
-----------------------------
During compile time one thing showing multiple behaviour is called as compile time polymorphism.
ex: method overloading, where during compilation, compiler will decide
which behaviour to be implemented so here methodname is same but depending
on type of args it shows different behaviour.
run()
run(int i)
run(char ch)
run(String s,int i)

Method Overloading Using Three Methods:
---------------------------------------
THE PROCESS OF DEVELOPING MULTIPLE METHODS WITH SAME NAME BUT DIFFERENT
ARGUMENTS LIST IS CALLED AS METHOD OVERLOADING.
"""

class Calculator:
    def add_two_numbers(self, a, b):
        """
        Adds two numbers.
        """
        return a + b

    def add_three_numbers(self, a, b, c):
        """
        Adds three numbers.
        """
        return a + b + c

    def add_four_numbers(self, a, b, c, d):
        """
        Adds four numbers.
        """
        return a + b + c + d


# Creating an object of the Calculator class
calc = Calculator()

# Calling the three methods with different numbers of arguments
result1 = calc.add_two_numbers(5, 10)       # Adds 5 + 10
result2 = calc.add_three_numbers(5, 10, 15) # Adds 5 + 10 + 15
result3 = calc.add_four_numbers(5, 10, 15, 20) # Adds 5 + 10 + 15 + 20

# Printing the results
print("Result of adding two numbers:", result1)         # Output: 15
print("Result of adding three numbers:", result2)       # Output: 30
print("Result of adding four numbers:", result3)        # Output: 50
