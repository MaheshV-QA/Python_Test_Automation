# The range() function is used to generate a sequence of numbers.
# It can take 1, 2, or 3 arguments in the form:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# ============================
# Example 1: One Argument (stop)
# range(stop) --> Starts from 0, ends at stop - 1
# ============================

print("Example 1: range(stop)")
for i in range(10):  # This will generate numbers from 0 to 9
    print(i)

print("\n" + "#" * 80)

# ============================
# Example 2: Two Arguments (start, stop)
# range(start, stop) --> Starts from 'start', ends at stop - 1
# ============================

print("Example 2: range(start, stop)")
for i in range(3, 10):  # This will generate numbers from 3 to 9
    print(i)

print("\n" + "#" * 80)

# ============================
# Example 3: Three Arguments (start, stop, step)
# range(start, stop, step) --> Starts from 'start', increments by 'step', stops before 'stop'
# ============================

print("Example 3: range(start, stop, step)")
for i in range(5, 15, 3):  # This will generate numbers: 5, 8, 11, 14
    print(i)
