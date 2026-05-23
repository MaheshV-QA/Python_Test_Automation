"""
1. Instance Variables:
If the value of a variable is varied from object to object, then such type of variables are called
instance variables.

====================================================

For every object a separate copy of instance variables will be created.
Where we can declare Instance variables:
1. Inside Constructor by using self variable
2. Inside Instance Method by using self variable
3. Outside of the class by using object reference variable
"""

class Test:
    def __init__(self):
        # Declaring instance variables inside the constructor
        self.a = 10
        self.b = 20

    def m1(self):
        # Declaring instance variables inside an instance method
        self.c = 30

# Creating an object of the Test class
t = Test()
# Calling the instance method to declare the instance variable 'c'
t.m1()
# Declaring an instance variable outside of the class using object reference
t.d = 40

# Printing the instance variables of the object
print(t.__dict__)  # Output: {'a': 10, 'b': 20, 'c': 30, 'd': 40}