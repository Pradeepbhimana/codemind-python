def rev(a):
    c=0
    while(a):
        c=c*10+a%10
        a//=10
    return c
    
    
a=int(input())
print(rev(a))
