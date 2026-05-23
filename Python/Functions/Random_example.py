# In Python, you can generate random numbers using the random module, 
# which provides a variety of functions to generate random numbers. 

import random

# 1. Generate a Random Integer
random_integer = random.randint(1, 10)
print("Random Integer between 1 and 10:", random_integer)

# 2. Generate a Random Float (between 0 and 1)
random_float = random.random()
print("Random Float between 0 and 1:", random_float)

# 3. Generate a Random Float within a Range
random_float_range = random.uniform(1, 10)
print("Random Float between 1 and 10:", random_float_range)

# 4. Randomly Select an Item from a List
items = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(items)
print("Random Item from the list:", random_item)

# 5. Generate a List of Random Integers (Unique)
random_integers = random.sample(range(1, 21), 5)
print("List of 5 unique random integers between 1 and 20:", random_integers)

# 6. Generate a List of Random Integers (Allow Duplicates)
random_integers_with_duplicates = random.choices(range(1, 21), k=5)
print("List of 5 random integers with possible duplicates between 1 and 20:", random_integers_with_duplicates)

# 7. Shuffle a List (In Place)
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(deck)
print("Shuffled List:", deck)

# 8. Set a Seed for Reproducibility
random.seed(42)  # Setting seed for reproducibility
random_integer_seeded = random.randint(1, 10)
print("Random Integer with seed (should be the same every run):", random_integer_seeded)
