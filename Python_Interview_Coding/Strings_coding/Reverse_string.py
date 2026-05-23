name = "hyderabad"
reverse_name = ""

# using slicing
print(name[::-1])

# using loop
for i in name:
    reverse_name = i+reverse_name

print(reverse_name)

# checking palidrome
print(name == reverse_name)

# printingbforward direction
print("Forward direction")
for a in name:
    print(a, end='')

# printing backward direction
print("Backward direction")
for b in name[::-1]:
    print(b,end='')



reversed_string = ""

for a in range(len(name) - 1, -1, -1):
    reversed_string += name[a]  # Append characters in reverse order

print(reversed_string)  # Output: "olleh"

################################################


word = "people tech group is a good company"

word1 = word.split()  # Splitting the sentence into words
output = ""  # Initialize an empty string

# Looping through the list in reverse order
for i in range(len(word1) - 1, -1, -1):
    output += word1[i] + " "

print(output.strip())  # Using strip() to remove the extra space at the end


# Output:company good a is group tech people

################################################
word = "RRSSTUV"

non_duplicate = " "

for i in word:
    if i not in non_duplicate:
        non_duplicate = non_duplicate + i
        
print(non_duplicate)

# Output: RSTUV
################################################
input_str = "Test in Progress"

a = input_str.split()
rev = []
for i in range(len(a)-1, -1, -1):
    rev.append(a[i][::-1])  # reverse each word and store in a list

print(' '.join(rev))

# Output: ssergorP ni tseT
