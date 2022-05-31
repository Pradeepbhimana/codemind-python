a=int(input())
b=list(map(int,input().split()))
c=abs(min(b))

for i in range(c,0,-1):
    d=0
    for j in b:
        if(j%i==0):
            d+=1
    if(d==a):
        print(i)
        break