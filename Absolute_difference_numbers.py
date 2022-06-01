def ab(a,b):
    c=a%pow(10,b)
    d=a
    co=0
    while(d!=0):
        co+=1
        d//=10
    c1=a//pow(10,co-b)
    return abs(c-c1)
a,b=map(int,input().split())
c=ab(a,b)
print(c)