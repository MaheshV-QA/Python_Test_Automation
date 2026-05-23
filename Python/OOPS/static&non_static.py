"""
1.Static Variable (Class Variable)
---------------------------------
* its belongs to class varable and shared by all objects of the class
* its outside  __init__(constructor) method
* accessed by ClassName.variable or self.variable.
* memoryStored once for the whole class.

--------------------------------------------------------------------------------------
2. Non-Static Variable (Instance Variable)
--------------------------------------------------
Belongs to: Each object separately.
Defined: Inside __init__ using self.
Accessed by: self.variable.
Memory: Each object gets its own copy.
Changes affect: Only that specific object, not others.

"""

class Dog:
    species = "Canine"  # Class attribute or static varable

    def __init__(self, name, age):
        self.name = name  # Instance attribute or non static varable
        self.age = age  # Instance attribute

dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly



