def feb(a):
    c,b=0,a
    while(b!=0):
        c+=1
        b//=10
    d=a
    e=1
    su=0
    while(c>=1):
        su=su+pow(d%10,c)
        d//=10
        c-=1
    if(su==a):
        return 1
    else:
        return 0        
        
a=int(input())
if(feb(a)):
    print(True)
else:
    print(False)
