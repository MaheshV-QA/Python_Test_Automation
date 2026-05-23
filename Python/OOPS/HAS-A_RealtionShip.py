"""
HAS-A relation ship is a relationship between two classes where one class contains the reference of another class
 
or 

One class containing the reference of another class is called as HAS-A
relationship.

"""

class Model:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_model_info(self):
        return f"Model: {self.name}, Year: {self.year}"

class Car:
    def __init__(self, model, color):
        self.model = model  # Car HAS-A Model
        self.color = color  # Car HAS-A Color

    def get_car_info(self):
        return f"{self.model.get_model_info()}, Color: {self.color}"

# Creating a Model object
car_model = Model("Toyota Corolla", 2023)

# Creating a Car object with a Model and Color
my_car = Car(car_model, "Red")

# Displaying car details
print(my_car.get_car_info())

# Output: Model: Toyota Corolla, Year: 2023, Color: Red