def pal(a):
    b=a
    c=0
    while(b!=0):
        c=c*10+b%10 
        b//=10
    if(c==a):
        return 1
    else:
        return 0
    
a=int(input())
b=a+1
while(pal(b)!=1):
    b+=1
c=a-1
while(pal(c)!=1):
    c-=1
if(abs(a-b)>abs(a-c)):
    print(c)
elif(abs(a-b)==abs(a-c)):
    print(c,b)
else:
    print(b)
    
