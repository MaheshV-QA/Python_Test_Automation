""" A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding itself."""

# Check if a number is a perfect number
n = 28  # Example number to check
sum_of_divisors = 0

# Loop through possible divisors to find the sum of divisors
for i in range(1, n):
    if n % i == 0:  # Check if i is a divisor of n
        sum_of_divisors += i

# Check if the sum of divisors equals the original number
if n == sum_of_divisors:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
print("   ")

print("################Print perfect numbers from 1 to 500###########")
print("   ")
print("Perfect numbers between 1 and 500:")
for i in range(1, 501):
    sum_of_divisors = 0  # Reset sum for each number
    for j in range(1, i):
        if i % j == 0:  # Check if j is a divisor of i
            sum_of_divisors += j
    if i == sum_of_divisors:  # Check if the sum of divisors equals the number
        print(i, "is a perfect number.")
