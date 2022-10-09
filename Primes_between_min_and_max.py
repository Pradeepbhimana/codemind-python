def pr(a):
    if(a<2):
        return 0
    else:
        for i in range(2,int(a**0.5)+1):
            if(a%i==0):
                return 0
        return 1
a=int(input())
l=list(map(int,input().split()))
mi=min(l)
ma=max(l)
f=0
k=0
for i in range(a):
    if(l[i]==mi and f==0):
        mi=i
        f=1
    if(l[i]==ma and k==0):
        ma=i
        k=1
k=0
if(mi>ma):
    mi,ma=ma,mi
for i in range(a):
    if(i>=mi and i<=ma ):
        if(pr(l[i])):
            k+=1
print(k)
        
        