"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

# Check if a number is prime or not
n = 13  # Example number to check
is_prime = True

# Loop to check for factors from 2 to n-1
for i in range(2, n):
    if n % i == 0:  # If n is divisible by i, it's not prime
        is_prime = False
        print(f"{n} is not a prime number.")
        break

# If no factors were found, it is prime
if is_prime:
    print(f"{n} is a prime number.")

# Print prime numbers between 2 and 50
print("Prime numbers between 2 and 50:")
for i in range(2, 51):
    is_prime = True  # Reset flag for each number
    for j in range(2, i):  # Check for factors up to the square root of i
        if i % j == 0:  # If i is divisible by j
            is_prime = False
            break
    if is_prime:  # If no factors were found, it's prime
        print(i)

############################################################################################
# the sum of prime numbers
prime_sum = 0

# Loop through numbers from 2 to 10
for i in range(2, 11):
    is_prime = True  # Assume the number is prime initially
    # Check for factors from 2 to i-1
    for j in range(2, i):
        if i % j == 0:  # If i is divisible by j, it's not prime
            is_prime = False
            break  # Exit the inner loop if a factor is found
    if is_prime:  # If the number is prime
        print(i)  # Print the prime number
        prime_sum += i  # Add the prime number to the sum

# Print the sum of prime numbers found
print("Sum of primes:", prime_sum)