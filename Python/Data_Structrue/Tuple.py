""""
1.Tuple is an immutable, ordered collection in Python,
defined using parentheses () (e.g., tpl = (1, 2, 3)).

2.It supports indexing, slicing, iteration, and methods like count() and index(),
but does not allow modifications (no append(), remove(),no extend etc.).

3.Tuples are faster than lists, memory-efficient, and commonly used for fixed data structures,
function returns, and dictionary keys.

Python Tuple Methods with Examples
"""

# Creating a sample tuple
tp = ()
tpl = (1, 2, 3, 4, 5, 2)

print("length of tuple :",len(tpl))

# 1. count() - Returns the number of occurrences of a value
count_2 = tpl.count(2)
print("count():", count_2)  # 2

# 2. index() - Returns the index of the first occurrence of a value
index_3 = tpl.index(3)
print("index():", index_3)  # 2

# Tuples are immutable, so they do not support methods like append(), remove(), pop(), sort(), etc.

# Tuple operations
# 3. Concatenation - Joining two tuples
tpl2 = (6, 7, 8)
concat_tpl = tpl + tpl2
print("Concatenation:", concat_tpl)  # (1, 2, 3, 4, 5, 2, 6, 7, 8)

# 4. Repetition - Repeating elements in a tuple
repeated_tpl = tpl * 2
print("Repetition:", repeated_tpl)  # (1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 5, 2)

# 5. Membership - Checking if an element exists in a tuple
exists = 3 in tpl
print("Membership (3 in tpl):", exists)  # True

# 6. Iteration - Looping through a tuple
print("Iteration:")
for item in tpl:
    print(item, end=" ")  # Output: 1 2 3 4 5 2
print()

# 7. Length - Finding the length of a tuple
length = len(tpl)
print("Length:", length)  # 6

# 8. Min & Max - Finding minimum and maximum values
min_val = min(tpl)
max_val = max(tpl)
print("Min:", min_val, "| Max:", max_val)  # Min: 1 | Max: 5

# 9. Conversion - Converting a tuple to a list and back
lst = list(tpl)
print("Converted to list:", lst)  # [1, 2, 3, 4, 5, 2]
tpl_again = tuple(lst)
print("Converted back to tuple:", tpl_again)  # (1, 2, 3, 4, 5, 2)
