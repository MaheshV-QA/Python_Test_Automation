"""
super:
-------
The super keyword in Python is used to call methods from a parent class inside a child class. 
This is useful when you want to reuse the methods of the parent class without rewriting them.

1.Avoids code duplication : No need to rewrite the parent class methods.
2. Allows method extension :You can add more functionality while still using the parent class method.
3. Supports multiple inheritance : Helps resolve ambiguity when multiple parent classes exist.

"""

class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):
        super().show()  # Calling parent method using super()
        print("This is the child class method.")

# Creating an object of Child class
c = Child()
c.show()
