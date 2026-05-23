"""
Python zip() Function Example
-----------------------------

The zip() function combines multiple iterables (like lists, tuples) into a single iterator of tuples.
It pairs elements based on their position/index.

If the input iterables are of unequal length, zip() stops creating pairs when the shortest iterable is exhausted.
"""

# Example 1: Basic zip() usage
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

combined = zip(names, scores)
print("Example 1: Combined list ->", list(combined))
# Output: [('Alice', 85), ('Bob', 90), ('Charlie', 95)]

# Example 2: Unequal length lists
a = [1, 2, 3]
b = ['a', 'b']

paired = zip(a, b)
print("Example 2: Unequal length ->", list(paired))
# Output: [(1, 'a'), (2, 'b')]

# Example 3: Using zip() in a for-loop
print("Example 3: Looping through zipped lists")
x_coords = [10, 20, 30]
y_coords = [5, 15, 25]

for x, y in zip(x_coords, y_coords):
    print(f"Point: ({x}, {y})")

# Example 4: Creating a dictionary using zip()
keys = ['id', 'name', 'score']
values = [101, 'David', 88]

data_dict = dict(zip(keys, values))
print("Example 4: Created dictionary ->", data_dict)
# Output: {'id': 101, 'name': 'David', 'score': 88}

"""
Summary:
---------
- zip() is useful for combining multiple sequences.
- zip() stops when the shortest input sequence is exhausted.
- You can convert the result into list(), tuple(), or dict() depending on your need.
"""

