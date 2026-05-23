def validate_parentheses(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching.values():  # Opening brackets
            stack.append(char)
        elif char in matching.keys():  # Closing brackets
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

# Example usage
string = "{[()]}"
print("Is valid:", validate_parentheses(string))  # Output: True
