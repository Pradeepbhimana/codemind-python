a=input()
a=a.lower()
b=""
for i in a:
    if(i not in b and i!=" "):
        b+=i
b=sorted(b)
print(len(b))