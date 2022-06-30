a=input()
a=a.lower()
b=""


for i in a:
    c=0
    for j in a:
        if(i==j and i!=' '):
            c+=1
    if(c==1):
        b+=i
b=sorted(b)
for i in b:
    print(i,end="")

    
    