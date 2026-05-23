data =['a','e','i','o','u']
name =  "mahesh is a tester"
data1 = []
for i in name:
    if i in data:
        data1.append(i)
data1 = ''.join(data1)
print(len(data1),data1)


# count the duplicate letters in 

name = "mahesh is a tester"

letter_count = {}
for letter in name:
    if letter.isalpha():  # Consider only alphabetic characters
        if letter in letter_count:
            letter_count[letter] += 1  # Increment count
        else:
            letter_count[letter] = 1  # Initialize count

duplicate = {}
for letter in letter_count:
    if letter_count[letter] > 1:  # Check if the count is greater than 1
        duplicate[letter] = letter_count[letter]

print(duplicate)
