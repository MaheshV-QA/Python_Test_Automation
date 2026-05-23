# ========================================
# **Lambda Function in Python**
# ========================================
# A lambda function is a small, anonymous function defined using the `lambda` keyword.
# It can take any number of arguments but has only a single expression.

# Syntax:
# lambda arguments: expression

# The lambda function evaluates the expression and returns the result.

# ========================================
# **Examples**
# ========================================

# 1. **Basic Lambda Example**
add_10 = lambda x: x + 10
print("Add 10 to 5:", add_10(5))  # Output: 15

# 2. **Lambda with Multiple Arguments**
multiply = lambda x, y: x * y
print("Multiply 3 by 4:", multiply(3, 4))  # Output: 12

# 3. **Lambda with Conditional Expression**
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Check if 5 is even or odd:", check_even(5))  # Output: Odd
print("Check if 8 is even or odd:", check_even(8))  # Output: Even

# 4. **Lambda in Sorting**
data = [(1, 3), (2, 2), (4, 1)]
data.sort(key=lambda x: x[1])
print("Sorted list by second element:", data)  # Output: [(4, 1), (2, 2), (1, 3)]

# 5. **Lambda with Higher-Order Functions (map, filter, reduce)**
from functools import reduce

nums = [1, 2, 3, 4]

# Using map() to square each number
squares = list(map(lambda x: x**2, nums))
print("Squares using map:", squares)  # Output: [1, 4, 9, 16]

# Using filter() to keep even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", evens)  # Output: [2, 4]

# Using reduce() to calculate the product of all elements
product = reduce(lambda x, y: x * y, nums)
print("Product using reduce:", product)  # Output: 24
