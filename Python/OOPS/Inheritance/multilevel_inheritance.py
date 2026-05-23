"""
In multilevel inheritance, a child class inherits from a parent class, 
and then another class inherits from that child class. 
The inheritance chain continues through multiple levels.


"""

class Animal:
    def eat(self):
        print("Animal eats.")

class Mammal(Animal):  # Mammal inherits from Animal
    def drink_milk(self):
        print("Mammal drinks milk.")

class Dog(Mammal):  # Dog inherits from Mammal
    def bark(self):
        print("Dog barks.")

# Creating an object of the Dog class
dog = Dog()
dog.eat()        # Output: Animal eats.
dog.drink_milk() # Output: Mammal drinks milk.
dog.bark()       # Output: Dog barks.
