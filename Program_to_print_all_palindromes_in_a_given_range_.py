def pal(a):
    c=0
    while(a!=0):
        c=c*10+a%10
        a=a//10
    return c
a=int(input())
b=int(input())
for i in range (a,b+1):
    if(i==pal(i)):
        print(i,end=" ")