def co(a):
    s=0
    while(a):
        s+=1
        a//=10
    return s
s=1000
b=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if(co(a[i])<s):
        s=co(a[i])
#print(s)
q=0
for i in range(len(a)):
    if(co(a[i])==s):
        q+=1
print(q)
        
    