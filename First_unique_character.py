a=input()
a=a.lower()
b=""

d=1
for i in a:
    c=0
    for j in a:
        if(i==j and i!=' '):
            c+=1
    if(c==1):
        print(i)
        d=0
        break
if(d==1):
    print(-1)
#b=sorted(b)


    
    