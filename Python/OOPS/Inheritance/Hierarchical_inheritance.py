"""
Hierarchical Inheritance Example with Parent Class
---------------------------------------------------
Demonstrating how child classes can use methods from the parent class
while adding their own behavior.
"""

# Base class (Parent)
class Animal:
    def speak(self):
        print("Animal makes a sound.")

# Derived class 1 (Child of Animal)
class Dog(Animal):
    def speak(self):
        # Call the parent class's speak method
        super().speak()  
        print("Dog barks.")

# Derived class 2 (Child of Animal)
class Cat(Animal):
    def speak(self):
        # Call the parent class's speak method
        super().speak()
        print("Cat meows.")

# Creating objects of Dog and Cat
dog = Dog()  # Dog object
cat = Cat()  # Cat object

# Calling the speak method of each object
print("Dog speaking:")
dog.speak()  # Calls Animal's speak method, then Dog's speak method.

print("\nCat speaking:")
cat.speak()  # Calls Animal's speak method, then Cat's speak method.

"""
super() Function:

super().speak() calls the speak method of the parent class (Animal) from the child class (Dog or Cat).
"""