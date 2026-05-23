# map_lambda.py
# ========================================
# **map() with Lambda Function**
# ========================================
# The `map()` function applies a given function to all items in an iterable.
# It returns a map object that can be converted to a list.
# Syntax:
# map(lambda arguments: expression, iterable)

# ========================================
# **Examples**
# ========================================
# 1. Square each number in a list
def square(x):
    return x ** 2

nums = [1, 2, 3, 4, 5]
squares = list(map(square, nums))
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]


# 2. Convert temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius = [0, 20, 30, 40]
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print("Fahrenheit:", fahrenheit)  # Output: [32.0, 68.0, 86.0, 104.0]


# 3. Double each element in the list
def multiply_by_two(x):
    return x * 2

nums = [1, 5, 10, 15]
doubled = list(map(multiply_by_two, nums))
print("Doubled numbers:", doubled)  # Output: [2, 10, 20, 30]


# 4. Capitalize all words in a list
def capitalize_word(word):
    return word.capitalize()

words = ["apple", "banana", "cherry"]
capitalized = list(map(capitalize_word, words))
print("Capitalized words:", capitalized)  # Output: ['Apple', 'Banana', 'Cherry']


# 5. Add 5 to each number in a list
def add_five(x):
    return x + 5

nums = [5, 10, 15, 20]
plus_five = list(map(add_five, nums))
print("Numbers after adding 5:", plus_five)  # Output: [10, 15, 20, 25]
