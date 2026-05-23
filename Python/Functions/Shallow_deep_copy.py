import copy

"""
Shallow copy:A shallow copy of an object creates a new object, 
but does not create copies of objects that are referenced within it.

Deep Copy :A deep copy creates a new object and recursively copies all objects found within it.

"""
print(__doc__)
print("shallow copy")
original_list = [1, 2, [3, 4]]

shallow_copied_list = copy.copy(original_list)

shallow_copied_list[2][0] = 'Modified'

print("Original List:", original_list)      # Output: [1, 2, ['Modified', 4]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [1, 2, ['Modified', 4]]

print("################# deep copy ###################")
original_list = [1, 2, [3, 4]]

deep_copied_list = copy.deepcopy(original_list)

# Modifying the nested list within the deep copy
deep_copied_list[2][0] = 'Modified'

print("Original List:", original_list)      # Output: [1, 2, [3, 4]]
print("Deep Copied List:", deep_copied_list)  # Output: [1, 2, ['Modified', 4]]


