"""
a class (child or subclass) to inherit attributes and methods from another class (parent or superclass).

Single Inheritance: A subclass inherits from one superclass.

Multiple Inheritance: A subclass inherits from multiple superclasses.

Multilevel Inheritance: A subclass inherits from a superclass, which itself inherits from another superclass.

Hierarchical Inheritance: Multiple subclasses inherit from a single superclass.

"""
# Parent Class
class Animal:
    def speak(self):
        return "I am an animal."

# Child Class
class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!
