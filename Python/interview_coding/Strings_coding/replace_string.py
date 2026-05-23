s="Learning Python is very difficult"
s1=s.replace("difficult","easy")
print(s)
print(s1)

a ="aababababababbbaaabbbaaababababa"
a1 =a.replace("b","a")

print(a,"\n",a1)

"""
Once we creates string object, we cannot change the content.This non changeable behaviour is
nothing but immutability. If we are trying to change the content by using any method, then with
those changes a new object will be created and changes won't be happend in existing object.
"""

s="abab"
print(s,"is available at :",id(s))
s=s.replace("a","b")
print(s,"is available at :",id(s))
# print(s1,"is available at :",id(s1))