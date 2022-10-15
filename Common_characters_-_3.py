a=input()
a=a.lower()
a=a.split()
b=a[0]
d=0
q=""
for i in b:
    c=0
    for j in a:
        if(i in j):
            c+=1
    if(c==len(a)):
        q+=i
        
if(len(q)==0):
    print("-1")
else:
    print(min(q))
    