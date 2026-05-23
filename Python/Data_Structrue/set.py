"""
A set in Python is an unordered, mutable collection of unique elements,
defined using {} or set().

Python Set Methods with Examples
"""

# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. add() - Adds an element to the set
set1.add(10)
print("add():", set1)  # {1, 2, 3, 4, 10}


# 2. remove() - Removes an element (raises error if not found)
set1.remove(2)
print("remove():", set1)  # {1, 3, 4, 10}

# 3. discard() - Removes an element (no error if missing)
set1.discard(5)  # No error even if 5 is not in the set
print("discard():", set1)

# 4. pop() - Removes and returns a random element
popped = set1.pop()
print("pop():", set1, "| Removed Element:", popped)

# 5. clear() - Removes all elements
set1.clear()
print("clear():", set1)  # {}

# Reset sets for further examples
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 6. union() - Combines two sets (returns a new set)
union_set = set1.union(set2)
print("union():", union_set)  # {1, 2, 3, 4, 5, 6}

# 7. intersection() - Common elements between sets
intersect_set = set1.intersection(set2)
print("intersection():", intersect_set)  # {3, 4}

# 8. difference() - Elements in set1 but not in set2
diff_set = set1.difference(set2)
print("difference():", diff_set)  # {1, 2}

diff_set0 = set2.difference(set1)
print("diff_2():" , diff_set0)

# 9. symmetric_difference() - Elements in either set1 or set2, but not both
sym_diff_set = set1.symmetric_difference(set2)
print("symmetric_difference():", sym_diff_set)  # {1, 2, 5, 6}

# 10. issubset() - Checks if set1 is a subset of set2
is_subset = {1, 2}.issubset(set1)
print("issubset():", is_subset)  # True

# 11. issuperset() - Checks if set1 is a superset of set2
is_superset = set1.issuperset({1, 2})
print("issuperset():", is_superset)  # True

# 12. isdisjoint() - Checks if sets have no common elements
is_disjoint = set1.isdisjoint({5, 6})
print("isdisjoint():", is_disjoint)  # True

# 13. copy() - Returns a shallow copy of the set
copy_set = set1.copy()
print("copy():", copy_set)  # {1, 2, 3, 4}
