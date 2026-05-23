# ========================================
# **filter() with Lambda Function**
# ========================================
# The `filter()` function filters elements from an iterable based on a condition.
# It returns only the elements that satisfy the condition.
# Syntax:
# filter(lambda arguments: expression, iterable)

# ========================================
# **Examples**
# ========================================

# 1. Filter even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)  # Output: [2, 4, 6, 8, 10]

# 2. Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, nums))
print("Numbers greater than 5:", greater_than_5)  # Output: [6, 7, 8, 9, 10]

# 3. Filter strings with more than 3 characters
words = ["hi", "hello", "cat", "dog", "elephant"]
long_words = list(filter(lambda x: len(x) > 3, words))
print("Words with more than 3 characters:", long_words)  # Output: ['hello', 'elephant']

# 4. Filter negative numbers
numbers = [-2, -1, 0, 1, 2, 3, -3]
negative_numbers = list(filter(lambda x: x < 0, numbers))
print("Negative numbers:", negative_numbers)  # Output: [-2, -1, -3]

# 5. Filter vowels from a list
letters = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
vowels = list(filter(lambda x: x in 'aeiou', letters))
print("Vowels:", vowels)  # Output: ['a', 'e', 'i', 'o', 'u']
