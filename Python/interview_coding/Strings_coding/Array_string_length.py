# Array of strings
array = ["apple", "kiwi", "banana", "cherry", "fig"]

# Sorting the array by length using sorted() and key=len
sorted_array = sorted(array, key=len)

# Printing the sorted array
print("Sorted by length:", sorted_array)


#2.method
# Array of strings
array = ["apple", "kiwi", "banana", "cherry", "fig"]

# Manual sorting based on string length
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if len(array[i]) > len(array[j]):
            # Swap elements if the current string is longer than the next
            array[i], array[j] = array[j], array[i]

# Print the sorted array
print("Sorted by length:", array)
