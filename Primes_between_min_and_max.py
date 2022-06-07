def pr(a):
    if(a<=2):
        return 0
    else:
        for i in range(2,a//2):
            if(a%i==0):
                return 0
                break
        else:
            return 1
        
a=int(input())
b=list(map(int,input().split()))
c=max(b)
d=min(b)
for i in range(a):
    if(b[i]==c):
        c1=i
    if(b[i]==d):
        d1=i
q=0
if(c1>d1):
    for i in range(d1,c1+1):
        if(pr(b[i])):
            q+=1
else:
    for i in range(c1,d1+1):
        if(pr(b[i])):
            q+=1
print(q)

