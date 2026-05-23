# Input list containing 0s and 1s
l1 = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]

# Initialize variables to keep track of the current count and maximum count of consecutive 1s
count = 0
max_count = 0

# Loop through each element in the list
for i in l1:
    if i == 1:  # If the element is 1, increment the current count
        count += 1
        if count > max_count:  # Update max_count if the current count is greater
            max_count = count
    else:
        count = 0  # Reset the count when encountering a 0

# Print the maximum count of consecutive 1s
print(max_count)
