"""The default seperator is space. 
The return type of split() method is List"""

name = "people tech"
s1 = name.split()

for i in s1:
    print(i)

# people
# tech

s="22-02-2018"
l=s.split('-')
for x in l:
    print(x)


# 22
# 02
# 2018

s='learning Python is very Easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())