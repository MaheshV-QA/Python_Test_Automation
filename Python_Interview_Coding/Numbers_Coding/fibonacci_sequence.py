# Initialize n for the number of terms in the Fibonacci sequence
n = 10 # You can change this value to generate more or fewer terms

# Initial two Fibonacci numbers
f1 = [0, 1]

# Generate the Fibonacci sequence starting from index 2 to n-1
for i in range(2,n):
    f = f1[-1] + f1[-2]  # Sum of the last two elements in the sequence
    f1.append(f)          # Append the new Fibonacci number to the list

# Print the Fibonacci sequence
print(f1)
print(len(f1))
print(f1[-1])
