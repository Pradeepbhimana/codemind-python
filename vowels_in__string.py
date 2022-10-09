a=input()
#a=a.lower()
b=""
for i in a:
    if i not in b and i !=" ":
        b+=i
for i in b:
    if i in "aeiouAEIOU":
        print(i,end=" ")