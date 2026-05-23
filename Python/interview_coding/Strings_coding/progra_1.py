# input: a4b3c2
# output: aaaabbbcc

a = "a4b3c2"
output = ""

# Loop through the string
for i in range(0, len(a), 2):  # Step by 2 to access the letter and the number
    char = a[i]  # Get the character (a, b, c)
    num = int(a[i+1])  # Get the number that follows the character and convert to int
    output += char * num  # Repeat the character 'num' times and add to the output

print(output)

##################################################################################################
a = "AABBBCCCCaaaaa"
# output: A2B4C4a5
output = ""
count = 1

for i in range(1,len(a)):
    if a[i] == a[i - 1]:
        count += 1
    else:
        output += a[i - 1] + str(count)
        count = 1

# Add the last group
output += a[-1] + str(count)

print(output)


####################################################################

# input: a4k3b2
# output:aeknbd

a = "a4k3b2"
output = ""

# Loop through the string, stepping by 2
for i in range(0, len(a), 2):
    char = a[i]  # Get the character (a, k, b)
    shift = int(a[i+1])  # Get the number that follows the character and convert to int
    # Calculate the shifted character with wrap-around if necessary
    new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))  
    output += new_char  # Add the shifted character to the output

print(output)


##########################################################

# Q9. Write a program to remove duplicate characters from the given input string?
# input: ABCDABBCDABBBCCCDDEEEF
# output: ABCDEF

s = "ABCDABBCDABBBCCCDDEEEF"

s1 = ""

for i in s:
    if i not in s1:
        s1 +=i

print(s1)

############################################################################
# input: ABCABCABBCDE
# output: A-3,B-4,C-3,D-1,E-1

s ="ABCABCABBCDE"

d = {}

for x in s:
    if x in d.keys():
        d[x] =d[x]+1
    else:
        d[x] =1

for k,v in d.items():
    print("{} = {} Times".format(k,v))

print("#################################################")

duplicate_list = ["apple", "banana", "apple", "orange", "banana","banana", "apple", "orange","banana", "apple", "orange"]
print(duplicate_list)
non_duplicate = {}

for item in duplicate_list:
    if item in d.keys():
        non_duplicate[item] = non_duplicate[item]+1
    else:
        non_duplicate[item] = 1

print(non_duplicate)
for a,b in non_duplicate.items():
    print("{} = {} Times".format(a,b))


