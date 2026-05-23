def is_balanced(expression):
    stack = []
    matching_elements = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in matching_elements:  # If it's an opening bracket
            stack.append(char)
        elif char in matching_elements.values():  # If it's a closing bracket
            # Check if stack is empty or top of the stack doesn't match
            if stack and matching_elements[stack[-1]] == char:
                stack.pop()  # Pop the matching opening bracket
            else:
                return False
            
    # If the stack is empty, parentheses are balanced
    return len(stack) == 0


# Test cases
expression1 = "({[]})"
expression2 = "([)]"
expression3 = "(()())"
expression4 = "((())"

print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
print(is_balanced(expression3))  # Output: True
print(is_balanced(expression4))  # Output: False
