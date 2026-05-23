'''
Python program to create a calculator class.
Include methods for basic arithmetic operations.
'''

class Calculator:

    def __init__(self, n1, n2) -> None:
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        return self.n1 + self.n2
    
    def subtraction(self):
        return self.n1 - self.n2
    
    def multiply(self):
        return self.n1 * self.n2
    
    def division(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Error: Division by zero is not allowed."
    
# Creating a Calculator object with two numbers
cal = Calculator(2, 7)

# Performing operations
print(f"Addition: {cal.addition()}")
print(f"Subtraction: {cal.subtraction()}")
print(f"Multiplication: {cal.multiply()}")
print(f"Division: {cal.division()}")
