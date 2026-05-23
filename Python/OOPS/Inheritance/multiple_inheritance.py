class Engine:
    def start_engine(self):
        return "Engine started!"

class Wheels:
    def wheel_type(self):
        return "Alloy wheels"

class Car(Engine, Wheels):  # Multiple Inheritance
    def car_details(self):
        return "Car with " + self.wheel_type() + " and " + self.start_engine()

# Creating an object of Car
my_car = Car()

# Accessing methods from both parent classes
print(my_car.car_details())
# Output: Car with Alloy wheels and Engine started!

"""
Python uses the Method Resolution Order (MRO) to determine the order 
in which classes are searched for methods or attributes
"""