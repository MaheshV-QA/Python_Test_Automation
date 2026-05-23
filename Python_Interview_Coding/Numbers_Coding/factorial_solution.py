# Iterative approach to calculate factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach to calculate factorial
def factorial_recursive(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    elif n < 0:
        print("undefined")
    else:
        return n * factorial_recursive(n - 1)  # Recursive step

# Test the functions
n = 5  # Example input
print(f"Factorial of {n} using iterative approach: {factorial_iterative(n)}")
print(f"Factorial of {n} using recursive approach: {factorial_recursive(n)}")
