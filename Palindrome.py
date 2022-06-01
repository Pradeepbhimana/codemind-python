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
if(pal(a)):
    print(True)
else:
    print(False)