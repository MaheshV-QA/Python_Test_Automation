"""
2. Run time polymorphism :
-------------------------
During Run/Execution time one thing showing multiple behaviour is called
as Run time polymorphism.
ex: method overriding , where there are multiple methods with same name,
during execution time only JVM will come to know which method to be executed
depending on type of object.


Method Overriding Example (Car Example)
----------------------------------------
A child class overrides a method of the parent class to provide specific behavior.

Rules For Overriding
---------------------
1. Inheritance is required.
2. The method name and arguments must be the same in both the parent and child classes.
3. The overridden method should not be final.

Why do we go for Overriding ??
A. When subclass want the properties of super class but does not want the
implementation of it. In such case, sub class can change implementation
by means of Overriding.
"""

class Parents:
    def car(self):  # Overridden method
        print("Blue color")

    def carname(self):
        print("Audi")

class Son(Parents):
    def car(self):  # Overriding method
        print("Black color")

class Daughter(Parents):
    def car(self):  # Overriding method
        print("Pink color")

    def carname(self):  # Overriding method
        print("Nano")

# Create objects
parent = Parents()
son = Son()
daughter = Daughter()

# Call methods
parent.car()        # Output: Blue color
parent.carname()    # Output: Audi

son.car()           # Output: Black color
son.carname()       # Output: Audi (Inherited from Parents)

daughter.car()      # Output: Pink color
daughter.carname()  # Output: Nano (Overridden)
