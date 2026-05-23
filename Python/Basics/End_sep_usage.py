# -----------------------------------------------------------
# Demonstration of `end` and `sep` parameters in the print() function
# -----------------------------------------------------------

# --- `end` Parameter ---

# By default, print() adds a newline character at the end (end="\n").
# This means each print statement will print output on a new line.

L = [1, 3, 6, 7]

# Printing numbers with default behavior (new line after each print)
for number in L:
    print("without end", number)

# Output:
# without end 1
# without end 3
# without end 6
# without end 7

# --- Using `end` to print on the same line ---

# The `end` parameter controls what is printed at the end of the statement.
# Here we set `end=" "` (a space) to print all numbers on the same line, separated by spaces.

print("\nUsing 'end' parameter:")
for number in L:
    print(number, end=" ")
# Output: 1 3 6 7

print("\n")  # Adding a line break for clarity


# --- `sep` Parameter ---

# The `sep` parameter controls what separates multiple arguments in a single print statement.

# Example: printing a date in DD/MM/YYYY format
print("Date example using 'sep':")
print('12', '12', '1990', sep='/')
# Output: 12/12/1990

# Another example: using a dash as a separator
print("Name example using 'sep':")
print('John', 'Doe', sep='-')
# Output: John-Doe

# -----------------------------------------------------------
# Summary:
# `end` -> what to print after each call to print() (default is newline).
# `sep` -> what to place between multiple arguments inside one print().
# -----------------------------------------------------------
