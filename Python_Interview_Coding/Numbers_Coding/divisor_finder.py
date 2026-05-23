def printDivisors(n):  
    divisors = []  # Renaming 'list' to 'divisors' to avoid conflict with Python's built-in 'list'
    for i in range(1, n + 1):
        if n % i == 0:  # If 'i' is a divisor of 'n'
            divisors.append(i)  # Add the divisor to the list
    return divisors

# Example usage
n = int(input("Enter a number: "))  # Convert input to an integer
print(printDivisors(n))  # Print the list of divisors
