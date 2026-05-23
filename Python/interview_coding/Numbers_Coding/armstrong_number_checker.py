"""An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own 
digits each raised to the power of the number of digits."""

n = 9474  # The number to check

# Get the number of digits in the number
pow = len(str(n))

sum = 0  # Initialize sum to 0
for digits in str(n):  # Loop through each digit in the number
    sum += int(digits) ** pow  # Add each digit raised to the power of the number of digits

# Check if the sum equals the original number
print(sum == n)  # True if it's an Armstrong number, False otherwise

# Print the number of digits in the number
print(len(str(n)))  # Output the number of digits 



#################### Regular Method ######################
def is_armstrong(number):
    # Find the number of digits
    n = len(str(number))
    
    # Initialize sum
    armstrong_sum = 0
    
    # Loop through each digit of the number
    temp = number
    while temp > 0:
        digit = temp % 10  # Extract the last digit
        armstrong_sum += digit ** n  # Raise it to the power of the number of digits and add
        temp = temp//10  # Remove the last digit
    
    # Check if the computed sum matches the original number
    return armstrong_sum == number

# Test cases
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")