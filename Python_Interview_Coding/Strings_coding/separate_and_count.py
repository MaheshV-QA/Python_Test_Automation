input_String = "Automation@$%^9645"

letters = 'a-zA-Z'
numbers = '0-9'
letters_count = ""
numbers_count = ""
special_char = ""

for i in input_String:
    if i.isalpha():  # Check if character is a letter
        letters_count += i
    elif i.isdigit():  # Check if character is a number
        numbers_count += i
    else:  # Otherwise, it's a special character
        special_char += i

# Print the count of each category
print(f"Letters Count: {len(letters_count)}")
print(f"Numbers Count: {len(numbers_count)}")
print(f"Special Characters Count: {len(special_char)}")
