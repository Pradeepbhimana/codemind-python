def rev(a):
    c=0
    while(a!=0):
        c=c*10+a%10
        a//=10
    return c
a=int(input())
c=a+1
while(rev(c)!=c):
    c+=1
d=a-1
while(rev(d)!=d):
    d-=1
if(c-a > a-d):
    print(d)
elif(c-a == a-d):
    print(d,c)
else:
    print(c)
    