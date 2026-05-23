def remove_character(input_string, char_to_remove):
    # Replace the given character with an empty string
    result = input_string.replace(char_to_remove, "")
    return result

# Example usage
string = "hello world"
char = "o"
new_string = remove_character(string, char)
print(f"Original string: {string}")
print(f"String after removing '{char}': {new_string}")



#method 2

input_string = "hello world"
char_to_remove = "o"

result = ""  # Initialize an empty string

# Loop through each character in the string
for char in input_string:
    if char != char_to_remove:  # If the character is not the one to remove
        result += char  # Add it to the result string

print(f"Original string: {input_string}")
print(f"String after removing '{char_to_remove}': {result}")
