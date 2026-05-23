arr = [0, 1, 2, 4, 5, 6, 7]  # 3 is missing
n = len(arr)  # Since the numbers are from 0 to n
total_sum = (n * (n + 1)) // 2 #28
arr_sum = sum(arr) #25
missing_number = total_sum - arr_sum

print(f"The missing number is: {missing_number}")

# Output: The missing number is: 3
# ==========================================================================================================

array = [50,52,53,54,55,56,57,58,59,62,63,64,65,67,68,69,70]

minimum = min(array)
maximum = max(array)
length = maximum-minimum
missing_number1 = []
for i in range(minimum,maximum+1):
    if i in array:
        pass
    else:
        missing_number1.append(i)

print(missing_number1)
# =============================================================================================================
        
