# Input number to check for palindrome
a = 121
n = a  # Store the original number for comparison
rev = 0  # Initialize the reverse variable

# Loop to reverse the number
while a > 0:
    rev = rev * 10
    rev = rev + a % 10  # Build the reversed number
    a = a // 10  # Remove the last digit from a

# Print the reversed number
print(f'Reversed number: {rev}')

# Check if the reversed number is equal to the original number
if rev == n:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
