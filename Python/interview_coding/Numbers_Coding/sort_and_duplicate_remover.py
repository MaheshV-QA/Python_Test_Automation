# Original list with duplicates
numbers = [9, 11, 12, 13, 1, 2, 3, 4, 1, 1, 2, 3, 4, 5, 14, 5, 6, 7, 8, 10, 10, 15, 15]

# Bubble sort implementation to sort the numbers in ascending order
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:  # Compare adjacent elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Swap if they are in the wrong order

# Print the sorted list
print("Sorted list:", list(set(numbers)))

# Print the maximum value, which is the last element after sorting
print("Maximum value:", numbers[-1])  # Last element after sorting
# Print the minimum value, which is the first element after sorting
print("Minimum value:", numbers[0])    # First element after sorting

# Calculate the average of the numbers and round it to the nearest integer
average = round(sum(numbers) / len(numbers))
print("Average (rounded):", average)

# Remove duplicates from the list
non_duplicate_list = []  # Initialize an empty list to store non-duplicate elements
for i in numbers:  # Iterate through the sorted list
    if i not in non_duplicate_list:  # Check if the element is not already in the new list
        non_duplicate_list.append(i)  # Add the unique element to the new list

# Print the list of non-duplicate elements
print("Non-duplicate list:", non_duplicate_list)
