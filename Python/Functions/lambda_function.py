"""
lambda arguments: expression

Lambda Function?
A lambda function is a small, anonymous function defined using the lambda keyword. 
It can have multiple arguments but only one expression.

->anonymous function
->using lambda keyword
->it takes no.of arguments
->its writes in single line
"""

# Lambda function for addition
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Using lambda in higher-order functions
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]
