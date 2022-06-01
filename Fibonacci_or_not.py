def feb(a):
    c=0
    d=[]
    
    a1=0
    d.append(a1)
    a2=1
    d.append(a2)
    
    while(c<a-2):
        a3=a1+a2
        d.append(a3)
        a1=a2
        a2=a3
        c+=1
    return d
        
a=int(input())
d=[]
d=feb(a)
for i in d:
    if(i==a):
        print(True)
        break
else:
    print(False)
