def remove_duplicates(strings):
    return list(set(strings))

# Example usage
array = ["apple", "banana", "apple", "orange", "banana"]
unique_array = remove_duplicates(array)

print("Array after removing duplicates:", unique_array)


#2. method
duplicate_list = ["apple", "banana", "apple", "orange", "banana"]

unique_list = []

for items in duplicate_list:
    if items not in unique_list:
        unique_list.append(items)

print(f'unique list of strings : {unique_list}')
