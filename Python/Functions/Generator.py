"""
A generator is a special type of iterative  function in Python that allows you to 
produce a sequence of values lazily (one value at a time) using the yield statement.
"""

def generate_numbers(n):
    for i in range(n):
        yield i  # Yield returns one value at a time

# Using the generator
gen = generate_numbers(5)
for num in gen:
    print(num)  # Outputs: 0, 1, 2, 3, 4

"""
differen b/w loops and generator

Lopps:  A normal loop generates all values at once and stores them in memory.
        Easy to use
        Consumes more memory (stores all values in a list).
        Slower for large datasets

Generator: A generator produces values one at a time and only when needed.
            Efficient memory usage
            Faster for large datasets
            Use the next() function to get the next value
            Can be used in a for loop & Can be paused and resumed
            Use the yield keyword to return values
            Use the return keyword to stop the generator
            Can be used to create infinite sequences
            Example: Fibonacci sequence generator
"""