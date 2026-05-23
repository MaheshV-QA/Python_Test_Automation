"""
Rearrange no.of possabilities and get greatest number
"""

n = 123987
length = len(str(n))
n = sorted(str(n),reverse=True)
n = ''.join(n)
print(n)


print(''.join(sorted(str(input()),reverse=True)))