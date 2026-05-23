# List 1
l1 = [1, 2, 3, 4, 5]

# List 2
l2 = [3, 4, 5, 6, 7]

# Combine both lists
l3 = l1 + l2

# Create a new list to hold unique elements
l4 = []
for i in l3:
    if i not in l4:  # Check if the element is not already in l4
        l4.append(i)  # Append the unique element to l4

# Print the list of unique elements
print("Unique elements from combined lists:", l4)


"""
get duplicatr elements
"""

my_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 3, 1]

duplicate_elements = []
unique_elements = []

for num in my_list:
    if num in unique_elements:
        duplicate_elements.append(num)
    
    else:
        unique_elements.append(num)

print("duplicate_elements",duplicate_elements)
print("unique_elements",unique_elements)
