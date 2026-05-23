# flatten_list_examples.py

# Flattening with isinstance() check
list6 = [1, (2, 3), {4, 5}, [6, 7], 8, 'Python', ['test1', 'test2'], {" "}]
flattened_list = []

for item in list6:
    if isinstance(item, (list, tuple, set)):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("Flattened list:", flattened_list)

# ----------------------------------------

# Method 1: Using a for loop
list1 = [[1, 2, 3], [4, 5, 6]]
newlist = []
for sublist in list1:
    for j in sublist:
        newlist.append(j)

print("For Loop Flatten:", newlist)

# ----------------------------------------

# Method 2: Using itertools.chain
import itertools

flat_list = list(itertools.chain.from_iterable(list1))
print("itertools Flatten:", flat_list)

# ----------------------------------------

# Method 3: Using list comprehension
flat_list_comp = [element for sublist in list1 for element in sublist]
print("List Comprehension Flatten:", flat_list_comp)
print(help('keywords'))
