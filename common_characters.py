a=input()
a=a.lower()
b=input()
b=b.lower()
c=""
d=""
for i in a:
    if(i not in c and i!=" "):
        c+=i
for i in c:
    if(i in b):
        d+=i
d=sorted(d)
if(len(d)==0):
    print("-1")
else:
    for i in d:
        print(i,end="") 