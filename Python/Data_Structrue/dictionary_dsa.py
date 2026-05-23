i = 1
n = 3  # Set the number of entries you want to input
a = dict()

while i <= n:
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    # Convert marks to integer
    a[name] = int(marks)  # You can use `float(marks)` if marks are decimals
    
    i += 1

print(a)
###################################