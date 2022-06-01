def fac(a):
    s=1
    while(a!=0):
        s*=a
        a-=1
    return s
def st(a):
    su=0
    b=a
    while(a!=0):
        su+=fac(a%10)
        a//=10
    if(su==b):
        return 1
    else:
        return 0
a=int(input())
if(st(a)):
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")
        