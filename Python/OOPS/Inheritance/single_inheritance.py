# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from the Animal class (single inheritance)
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the constructor of the parent class (Animal)
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

# Creating an object of the Dog class
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # Output: Buddy barks.
