a = "people tech group"
l = a.split()
l1 =[]
print(len(l))
for i in range(len(l)):
    l1.append(l[i][::-1])

op = ' '.join(l1)
print(op)

a = "people tech group.quest global ltd"
index1 = a.index(".")
print(index1)
a1 = a.split('.')
l1 = []

for i in range(len(a1)):
    l = a1[i].split()  # Split each section by spaces into words
    for j in range(len(l)):  # Loop over the list of words
        l1.append(l[j][::-1])  # Reverse each word and append it to l1
    # if i != len(a1) - 1:  # If it's not the last section, add a period after reversing
    #     l1.append('.') 

l1 = ' '.join(l1)  # Join the reversed words with space
l2 = l1[:index1] +"."+l1[index1+1:]
print(l2)
