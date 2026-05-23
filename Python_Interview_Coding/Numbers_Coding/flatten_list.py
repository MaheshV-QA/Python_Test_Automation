"""isinstance(): This checks whether an item is a list. If it is, 
the extend() method is used to unpack and add the elements of that sublist into the flattened_list."""


# Input list with a mix of integers, sublists, and strings
list6 = [1, (2, 3), {4, 5}, [6, 7], 8, 'Python', ['test1', 'test2'],{" "}]

# Initialize an empty list to store the flattened result
flattened_list = []

# Loop through each item in the list
for item in list6:
    if isinstance(item, (list, tuple,set)):  # Check if the item is a list
        flattened_list.extend(item)  # If it's a list,tuple,set, extend the flattened list with its elements
    else:
        flattened_list.append(item)  # If it's not a list, simply append the item

# Print the flattened list
print(flattened_list)
