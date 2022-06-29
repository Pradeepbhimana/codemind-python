def rev(a):
    if(a>=0):
        
        c=0
        while(a!=0):
            c=c*10+a%10
            a//=10
        return c
    else:
        a=-a
        c=0
        while(a!=0):
            c=c*10+a%10
            a//=10
        return -c
a=int(input())
c=rev(a)
print(c)