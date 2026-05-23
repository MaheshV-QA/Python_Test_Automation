# ===========================
"""
    A decorator is a function that adds extra functionality 
    to an existing function without modifying it.
"""

# =========================================
# Decorator Example
# ======================================
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, World!")

say_hello()

# OUTPUT

# Before the function call
# Hello, World!
# After the function call




