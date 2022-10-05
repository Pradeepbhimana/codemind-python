def su(a):
    s=0
    while(a):
        s=s+(a%10)*(a%10)
        a//=10
    return s
a=int(input())
s=su(a)
while(s//10!=0):
    s=su(s)
if(s==1 or s==7):
    print(True)
else:
    print(False)