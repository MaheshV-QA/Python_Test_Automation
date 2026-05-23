# Input list of numbers
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize two lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the list to separate even and odd numbers
for num in list2:
    if num % 2 == 0:  # Check if the number is even
        even_numbers.append(num)
    else:             # Otherwise, it is odd
        odd_numbers.append(num)

# Print the even and odd numbers
print(f'Even numbers are: {even_numbers}')
print(f'Odd numbers are: {odd_numbers}')

# Alternative one-liner to calculate the sum of even and odd numbers
even_sum = sum([i for i in list2 if i % 2 == 0])
odd_sum = sum([i for i in list2 if i % 2 != 0])

# Print the sums of even and odd numbers
print(f'Sum of even numbers: {even_sum}')
print(f'Sum of odd numbers: {odd_sum}')

##################################################################################################
# Given string of objects  find the sum of all possiable given digits      company name :zoho
num = 1546827
even_sum = 0
odd_sum = 0
odd_list = []

for i in str(num):  # Convert the number to a string to loop through each digit
    if int(i) % 2 != 0:  # If the digit is odd
        odd_list.append(int(i))  # Add the odd digit to the odd_list
        odd_sum += int(i)  # Add the odd digit to the odd_sum
    else:  # If the digit is even
        even_sum += int(i)  # Add the even digit to the even_sum


print(f'Even sum: {even_sum}')
print(f'Odd sum: {odd_sum}')
print(f'Odd digits: {odd_list}')

print(odd_list)
