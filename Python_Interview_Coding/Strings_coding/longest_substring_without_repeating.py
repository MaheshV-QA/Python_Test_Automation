"""Find the length of the longest substring without repeated characters given a string s"""

# Given string
s = "abcabcab"

# Initialize variables
s1 = ""  # Temporary substring to store unique characters
longest_substring = ""  # To store the longest substring without repeating characters

for i in s:
    if i not in s1:
        # Add character to the current substring if it's not repeated
        s1 += i
    else:
        # If a repeated character is found, check if the current substring is the longest
        if len(s1) > len(longest_substring):
            longest_substring = s1
        
        # Remove the part up to (and including) the first occurrence of the repeated character
        s1 = s1.replace(s1,'') + i  # Keep characters after the repeated one and add the new character

# Output the longest substring and its length
print("Longest Substring Without Repeating Characters:", longest_substring)
print("Length:", len(longest_substring))
