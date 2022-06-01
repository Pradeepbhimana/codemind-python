def s(a):
    b=a
    su=0
    while(b!=0):
        su+=b%10
        b//=10
    return su
def p(a):
    b=a
    su=1
    while(b!=0):
        su*=b%10
        b//=10
    return su
a=int(input())
if(s(a)==p(a)):
    print("Spy Number")
else:
    print("Not Spy Number")
