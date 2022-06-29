def pr(a):
    if(a<=1):
        return 0
    else:
        for i in range(2,a):
            if(a%i==0):
                return 0
        else:
            return 1
def re(a):
    c=0
    while(a):
        c=c*10+a%10
        a//=10
    return c
a=int(input())
if(pr(a)):
    if(pr(re(a))):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
