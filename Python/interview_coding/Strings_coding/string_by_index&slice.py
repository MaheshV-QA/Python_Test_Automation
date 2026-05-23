s = "mahesh"
i =0

for x in s:
    print(i,x)
    i =i+1

# by slice

print(s[::-1])
reverse1 = ""
for a in range(len(s)-1,-1,-1):
    reverse1 =reverse1 + s[a]
print(a)