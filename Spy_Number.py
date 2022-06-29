
def pr(a):
    c=1
    while(a!=0):
        c*=a%10
        a//=10
    return c
def s(a):
    b=0
    while(a!=0):
        b+=a%10
        a//=10
    return b
a=int(input())
if(pr(a)==s(a)):
    print("Spy Number")
    #print(pr(a),s(a))
else:
    print("Not Spy Number")