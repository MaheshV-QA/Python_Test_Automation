"""
#### ** List (Ordered, Mutable, Allows Duplicates)**  
A **list** is a collection of elements that maintain order and can be modified. 

Python List Methods with Examples
"""

# 1. append() - Adds an element to the end of the list
lst = [1, 2, 3]
lst.append(4)
print("append():", lst)  # [1, 2, 3, 4]

# 2. extend() - Adds multiple elements from an iterable
lst.extend([5, 6, 7])
print("extend():", lst)  # [1, 2, 3, 4, 5, 6, 7]

# 3. insert() - Inserts an element at a specific index
lst.insert(2, 99)
print("insert():", lst)  # [1, 2, 99, 3, 4, 5, 6, 7]

# 4. remove() - Removes the first occurrence of a value
lst.remove(99)
print("remove():", lst)  # [1, 2, 3, 4, 5, 6, 7]

# 5. pop() - Removes and returns an element at the given index (default: last)
popped = lst.pop()
print("pop():", lst, "| Removed Element:", popped)  # [1, 2, 3, 4, 5, 6] | Removed Element: 7

# 6. clear() - Removes all elements from the list
lst.clear()
print("clear():", lst)  # []

# Reset list for further examples
lst = [10, 20, 30, 40, 50, 20]

# 7. index() - Returns the index of the first occurrence of a value
index = lst.index(20)
print("index():", index)  # 1

# 8. count() - Returns the number of occurrences of a value
count = lst.count(20)
print("count():", count)  # 2

# 9. sort() - Sorts the list in ascending order
lst.sort()
print("sort():", lst)  # [10, 20, 20, 30, 40, 50]

# 10. sorted() - Returns a new sorted list without modifying the original
unsorted_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(unsorted_list)
print("sorted():", sorted_list, "| Original List:", unsorted_list)  # [1, 1, 3, 4, 5, 9]

# 11. reverse() - Reverses the list in place
lst.reverse()
print("reverse():", lst)  # [50, 40, 30, 20, 20, 10]

# 12. copy() - Returns a shallow copy of the list
copy_lst = lst.copy()
print("copy():", copy_lst)  # [50, 40, 30, 20, 20, 10]

# 13. del statement - Deletes elements from the list using index
del lst[2]
print("del statement:", lst)  # [50, 40, 20, 20, 10]

# 14. List slicing - Removes last element using slicing
lst = lst[:-1]
print("List slicing (remove last element):", lst)  # [50, 40, 20, 20]

# =======================================================================================================================================================
# extend_vs_append_simple.py
# ================
# append()--> will add single value
# extend ()--> will add  2 or more values
# Using append()
print("Using append():")
my_list = [1, 2, 3]
print("Before append:", my_list)

# Append a single element
my_list.append(4)
print("After appending 4:", my_list)

# Append a list (adds it as a single element)
my_list.append([5, 6])
print("After appending [5, 6]:", my_list)

print("\nUsing extend():")
# Using extend()
my_list = [1, 2, 3]
print("Before extend:", my_list)

# Extend with another list (adds each item separately)
my_list.extend([4, 5, 6])
print("After extending with [4, 5, 6]:", my_list)

# Extend with a string (adds each character separately)
my_list.extend("78")
print("After extending with '78':", my_list)

# Summary of the difference
print("\nSummary:")
print("- append() adds a single item to the list (even if it’s a list).")
print("- extend() adds each element of an iterable separately to the list.")

# ===============================================================================================================================================
# list_operations.py

# -------------------------
# sort vs sorted
# -------------------------

# Using sort() - modifies the original list
my_list = [3, 1, 4, 1, 5]
print("Original list (before sort()):", my_list)

my_list.sort()  # Sorts the list in place
print("List after sort():", my_list)

# Using sorted() - creates a new sorted list without modifying the original
another_list = [3, 1, 4, 1, 5]
print("\nOriginal list (before sorted()):", another_list)

new_sorted_list = sorted(another_list)  # Returns a new sorted list
print("New sorted list:", new_sorted_list)
print("Original list remains unchanged:", another_list)

# -------------------------
# reverse vs reversed
# -------------------------

# Using reverse() - modifies the original list in place
my_list = [1, 2, 3, 4, 5]
print("\nOriginal list:", my_list)

my_list.reverse()  # Reverses the list in place
print("List after reverse():", my_list)

# Using reversed() - returns an iterator, original list remains unchanged
another_list = [1, 2, 3, 4, 5]
print("\nOriginal list:", another_list)

reversed_list = list(reversed(another_list))  # Convert iterator to list
print("Reversed list using reversed():", reversed_list)
print("Original list remains unchanged:", another_list)

# -------------------------
# Sorting in Reverse Order
# -------------------------

# Using sort() with reverse=True - modifies the list in place
list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list1.sort(reverse=True)  # Sorts in reverse (descending) order
print("\nList after sorting in reverse order:", list1)

# Using sort() with reverse=True and capturing the result
list1 = [2, 5, 6, 8, 1, 8, 9, 11]
list2 = list1.sort(reverse=True)  # Returns None, modifies list1 in place
print("list2 after sorting (should be None):", list2)
print("Original list1 after sorting:", list1)

# -------------------------
# Notes:
# 1. sort():
# - Modifies the list in place (does not return a new list).
# - Works only on lists.
# - Can sort in reverse order using reverse=True.
#
# 2. sorted():
# - Returns a new sorted list, does not modify the original list.
# - Works with any iterable (lists, tuples, dictionaries, sets, etc.).
#
# 3. reverse():
# - Reverses the list in place (modifies the original list).
# - Works only on lists.
#
# 4. reversed():
# - Returns an iterator (does not modify the original list).
# - Works with any iterable (lists, tuples, strings, etc.).
# -------------------------
