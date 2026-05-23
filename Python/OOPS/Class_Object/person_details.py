'''
2. Write a Python program to create a person class. Include attributes like name, country and date of birth. 
Implement a method to determine the person's age.

'''
from datetime import date


print(__doc__)

class My_Details:

    def __init__(self,name,country,date_of_birth):
        self.name =name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
person1 = My_Details("mahesh","india",date(1996,12,22))

print(f"name,{person1.name}")
print(f"country ,{person1.country}")
print(f"date of birth,{person1.date_of_birth}")
print(f"calucalte age ,{person1.calculate()}")
