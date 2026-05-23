"""
Exception handling allows you to manage errors gracefully in your code using try, except, else, and finally blocks. 
It helps to prevent the program from crashing and provides a way to handle errors effectively.

try:   Contains code that may raise exceptions.
except:   Catches and handles specific exceptions.
else:     Executes if the try block does not raise an exception.
finally:   Executes regardless of whether an exception occurred, useful for cleanup.

"""



def divide_numbers(num1, num2):
    """
    Divides two numbers with exception handling.
    """
    try:
        result = num1 / num2  # May raise an exception
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")  # Handle division by zero
    except TypeError:
        print("Error: Invalid input types! Please provide numbers.")  # Handle type errors
    else:
        print(f"The result of {num1} divided by {num2} is: {result}")  # No exceptions
    finally:
        print("Execution of the divide_numbers function is complete.")  # Always runs

# Test the function with various inputs
divide_numbers(10, 2)   # Valid input
divide_numbers(10, 0)   # Division by zero
divide_numbers(10, 'a') # Invalid input type
