"""The split() method is used to divide a string into a list of substrings based on a specified delimiter"""

text = "Hello, how are you?"
# Split the string by spaces
words = text.split()
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']

# Split by a specific delimiter
csv_line = "apple,banana,cherry"
fruits = csv_line.split(',')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

##################################################################################################################################
"""The join() method is used to concatenate a list of strings into a single string, with a specified separator between each string."""


words = ['Hello', 'how', 'are', 'you?']
# Join the list of words with a space
sentence = ' '.join(words)
print(sentence)  # Output: Hello how are you?

# Join with a different separator
csv = ', '.join(words)
print(csv)  # Output: Hello, how, are, you?
