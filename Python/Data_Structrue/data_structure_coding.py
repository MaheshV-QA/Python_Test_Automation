# -----------------------------------------------------------
# Merging Two Dictionaries in Python
# Method 1: Using `|` (pipe) operator - introduced in Python 3.9
# Method 2: Using `**` unpacking - works in Python 3.5+
# -----------------------------------------------------------

# Sample dictionaries
name1 = {"Kelly": 23, "Derick": 14, "John": 7}
name2 = {"Ravi": 45, "Mpho": 67}

# --- Method 1: Using | (Pipe Operator) ---
# This merges two dictionaries. If there are duplicate keys,
# the value from the second dictionary will overwrite the first.

names = name1 | name2
print("Merged using | operator:")
print(names)  # Output: {'Kelly': 23, 'Derick': 14, 'John': 7, 'Ravi': 45, 'Mpho': 67}

# --- Method 2: Using ** unpacking ---
# The double asterisk operator unpacks both dictionaries into a new one.
# Works the same way as | in terms of key overwriting.

names = {**name1, **name2}
print("\nMerged using ** unpacking:")
print(names)  # Output: {'Kelly': 23, 'Derick': 14, 'John': 7, 'Ravi': 45, 'Mpho': 67}

# -----------------------------------------------------------
# Note:
# - Both methods return a new merged dictionary.
# - If duplicate keys exist, the last one will overwrite the earlier ones.
# - `|` operator requires Python 3.9 or higher.
# - `**` unpacking works from Python 3.5 onwards.
# -----------------------------------------------------------
