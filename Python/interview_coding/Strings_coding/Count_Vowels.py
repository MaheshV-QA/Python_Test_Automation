# Function to count the number of vowels in a given string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage of count_vowels function
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is {vowel_count}")

# ======================================================

# Simple code to count vowels in a string and print each vowel
vowels = "aeiouAEIOU"
word = "Hello, World!"
count = 0
for char in word:
    if char in vowels:
        print(char)
        count += 1
print(f'The number of vowels in {word} is {count}')

# ======================================================

# This script counts the number of times a specific character occurs in a given word
word = "programming"
character = "m"
count = 0
for char in word:
    if char == character:
        count += 1
print(f'The number of times {character} occurred in {word} is {count}')