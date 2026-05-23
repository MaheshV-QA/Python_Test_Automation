# reduce_lambda.py
# ========================================
# **reduce() with Lambda Function**
# ========================================
# The `reduce()` function from the `functools` module applies a function 
# cumulatively to the items of an iterable, from left to right, 
# reducing the iterable to a single value.
# Syntax:
# reduce(lambda arguments: expression, iterable)

from functools import reduce

# ========================================
# **Examples**
# ========================================

# 1. Calculate the product of all elements in a list
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Product of all elements:", product)  # Output: 24

# 2. Find the sum of all elements in a list
sum_total = reduce(lambda x, y: x + y, nums)
print("Sum of all elements:", sum_total)  # Output: 10

# 3. Find the maximum element in a list
nums = [5, 3, 8, 6, 2]
maximum = reduce(lambda x, y: x if x > y else y, nums)
print("Maximum element:", maximum)  # Output: 8

# 4. Concatenate strings in a list
words = ["Hello", "world", "using", "reduce"]
sentence = reduce(lambda x, y: x + " " + y, words)
print("Concatenated string:", sentence)  # Output: "Hello world using reduce"

# 5. Calculate factorial of a number using reduce
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"Factorial of {n}:", factorial)  # Output: 120
