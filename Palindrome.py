def rev(a):
    c=0
    while(a!=0):
        c=c*10+a%10
        a//=10
    return c
a=int(input())
if(a==rev(a)):
    print(True)
else:
    print(False)