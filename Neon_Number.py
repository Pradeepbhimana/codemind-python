def sd(a):
    b=a
    su=0
    while(b!=0):
        su+=b%10
        b//=10
    return su
a=int(input())
if(a==sd(pow(a,2))):
    print("Neon Number")
else:
    print("Not Neon Number")