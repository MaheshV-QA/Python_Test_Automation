# Input list of numbers
list3 = [101,10, 54, 94, 99, 24, 73, 11, 77, 63, 95,1]

# Initialize max_number and min_number with the first element of the list
max_number = list3[0]
min_number = list3[0]

# Loop through the list to find the maximum and minimum numbers
for num in list3:
    if num > max_number:  # If current number is greater than max_number, update max_number
        max_number = num
    elif num < min_number:  # If current number is smaller than min_number, update min_number
        min_number = num

# Print the maximum and minimum numbers
print(f'Max number is: {max_number}')
print(f'Minimum number is: {min_number}')

# Alternative: Using Python's built-in functions to find min and max directly
print(f'Using built-in functions:')
print(f'Max number is: {max(list3)}')
print(f'Minimum number is: {min(list3)}')
