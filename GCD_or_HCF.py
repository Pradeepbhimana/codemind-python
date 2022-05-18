def hcf(a,b):
    if(a>b):
        c=a
        while True:
            if a%c==0 and b%c==0:
                return c
            else:
                c-=1
    else:
        c=b
        while True:
            if a%c==0 and b%c==0:
                return c
            else:
                c-=1
        
a,b=map(int,input().split())
c=hcf(a,b)
print(c)
