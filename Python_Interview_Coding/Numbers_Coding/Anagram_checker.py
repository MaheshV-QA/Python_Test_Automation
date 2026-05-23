# An anagram is a word or phrase formed by rearranging the letters of another

a = "Silent"
a = a.lower()  # Convert string 'a' to lowercase
b = "Listen"
b = b.lower()  # Convert string 'b' to lowercase

# Check if both words have the same length and sorted characters are the same
print(len(a) == len(b))  # Check if lengths are equal
print(sorted(a) == sorted(b))  # Check if sorted characters are equal

# Custom anagram check using a loop
is_anagram = True  # Initialize the flag for checking

for i in a:  # Iterate through each character in 'a'
    if i not in b:  # If a character from 'a' is not in 'b'
        print("False")  # Print "False" and mark as not an anagram
        is_anagram = False
        break  # Exit the loop as soon as a mismatch is found

if is_anagram:  # If no mismatches were found
    print("True")  # Print "True", meaning the words are anagrams
