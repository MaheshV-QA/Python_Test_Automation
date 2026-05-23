# count_item_occurrences.py

"""
Counting Item Occurrences:

If you want to know how many times an item appears in an iterable,
you can use the Counter class from the collections module.
Counter will return a dictionary with elements as keys and their counts as values.
"""

# count_occurrences.py

from collections import Counter

# Using Counter
list1 = ['John', 'Kelly', 'Peter', 'Moses', 'Peter']
count_peter = Counter(list1).get("Peter")
print(f'The name Peter appears {count_peter} times.')

# =================================================================================
# ====================================================================================

# Using a for loop
count = 0
for name in list1:
    if name == 'Peter':
        count += 1

print(f'The name Peter appears {count} times.')

