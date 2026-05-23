"""
decorators:

Decorators in Python are a powerful feature that allows me to modify or enhance the behavior of functions or methods without changing their actual code. 
They are functions that take another function as an argument and return a new function with added functionality. 
I use decorators frequently when I want to add reusable functionality to existing code, like logging, authentication, or caching.

"""
# To create a simple decorator, I define a function that takes another function as an argument. 
# Inside this decorator function, I define a nested function that adds the desired behavior, 
# then return this nested function.



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# In this example, the  my_decorator  function modifies the behavior of  say_hello  
# by printing additional messages before and after calling it. 
# I used the  @my_decorator  syntax to apply the decorator, which is a clean and readable way to enhance the function.

# Decorators can also accept arguments. When I need to pass arguments to a decorator, I
#  add an extra layer of nesting. This flexibility makes decorators one of the most versatile features in Python,
#  allowing me to write cleaner, more maintainable code.