#Write a code to return list of tuples where sum of tuple elements should be equal to given sum 
# Ex: L = [1,2,3,4,5] target_sum= 5 O/p [(2,3),(1,4)]

L = [0,2,3,4,5,6,1]
output =[]
target_sum =5

for i in range(len(L)):
    for j in range(i+1,len(L)):
        if i + j == target_sum:
            result = (i,j)
            output.append(result)
print(output)






        