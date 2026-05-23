#1.move all zeros to one end
list1 = [1,0,2,0,2,3,0]
zeros =[]
non_zeros =[]
for i in list1:
    if i==0:
        zeros.append(i)
    else:
        non_zeros.append(i)
print(non_zeros+zeros)

# non_zeros = [i for i in list1 if i !=0]
# zeros =list1.count(0)
# print(non_zeros + zeros*[0])

#############################################################################
n = 12345892345678861
while len(str(n)) > 1:  # Continue until the number becomes a single digit
    sum_digits = 0
    for digit in str(n):  # Iterate over each digit in the number
        sum_digits += int(digit)  # Convert each character to an integer and sum it
    n = sum_digits  # Update n to be the sum of the digits
print(n)  # Output the result