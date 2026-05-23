"""
# A dictionary in Python is a mutable, dynamic, and unordered collection of key-value pairs.
# Each key must be unique, and it maps to a corresponding value.
# Dictionaries are optimized for quick lookups, updates, and deletions.
# They are created using curly braces {} or the dict() constructor.
# Indexing and slicing are not possible in dictionaries.

"""
# creating empty dictionary
d1 = {}
d2 = dict()
print("creating empty list", type(d1))  # Output: creating empty list <class 'dict'>
print("creating empty list", type(d2))  # Output: creating empty list <class 'dict'>

# 1. Creating a dictionary
my_dict = {"name": "John", "age": 30}
print("Dictionary:", my_dict)  # Output: Dictionary: {'name': 'John', 'age': 30}

# 2. Accessing values with dict[key]
print("Name:", my_dict["name"])  # Output: Name: John

# 3. Using get() to access values safely
print("Age:", my_dict.get("age"))  # Output: Age: 30
print("Gender (with default):", my_dict.get("gender", "Not Found"))  # Output: Gender (with default): Not Found

# If the key is available then returns the corresponding value otherwise returns None.It wont raise any error.

# 4. Getting keys
print("Keys:", my_dict.keys())  # Output: Keys: dict_keys(['name', 'age'])

# 5. Getting values
print("Values:", my_dict.values())  # Output: Values: dict_values(['John', 30])

# 6. Getting items
print("Items:", my_dict.items())  # Output: Items: dict_items([('name', 'John'), ('age', 30)])

# 7. Updating dictionary with update()
new_values={"age": 35, "location": "New York"}
my_dict.update(new_values)
print("Updated Dictionary:", my_dict)  # Output: Updated Dictionary: {'name': 'John', 'age': 35, 'location': 'New York'}

# 8. Removing a key-value pair using pop()
removed_value = my_dict.pop("age")
print("Removed Value:", removed_value)  # Output: Removed Value: 35
print("Dictionary after pop:", my_dict)  # Output: Dictionary after pop: {'name': 'John', 'location': 'New York'}

# 9. Removing last inserted item using popitem()
item = my_dict.popitem()
print("Popped Item:", item)  # Output: Popped Item: ('location', 'New York')
print("Dictionary after popitem:", my_dict)  # Output: Dictionary after popitem: {'name': 'John'}

# 10. Clearing the dictionary
my_dict.clear()
print("Dictionary after clear:", my_dict)  # Output: Dictionary after clear: {}

# 11. Copying a dictionary
original = {"name": "John", "age": 30}
copy_dict = original.copy()
print("Copied Dictionary:", copy_dict)  # Output: Copied Dictionary: {'name': 'John', 'age': 30}

# 12. Creating a dictionary from keys using fromkeys()
keys = ["name", "age", "location"]
default_dict = dict.fromkeys(keys, "N/A")
print("Dictionary from keys:", default_dict)  # Output: Dictionary from keys: {'name': 'N/A', 'age': 'N/A', 'location': 'N/A'}

# 13. Using setdefault()
value = copy_dict.setdefault("gender", "Unknown")
print("Value returned by setdefault:", value)  # Output: Value returned by setdefault: Unknown
print("Dictionary after setdefault:", copy_dict)  # Output: Dictionary after setdefault: {'name': 'John', 'age': 30, 'gender': 'Unknown'}

# 14. Length of a dictionary
print("Length of Dictionary:", len(copy_dict))  # Output: Length of Dictionary: 3

# 15. Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension (squares):", squares)  # Output: Dictionary Comprehension (squares): {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 16.# Deleting a key from the dictionary
a = {"name": "Alice", "age": 25, "marks": 90}
del a["age"]

print(a)  # Output: {'name': 'Alice', 'marks': 90}

