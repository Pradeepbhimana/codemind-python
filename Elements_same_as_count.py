a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if(i not in c):
        c.append(i)
e=0
q=[]
for i in c:
    d=0
    for j in b:
        if(i==j):
            d+=1
    if(d==i):
        q.append(i)
        e=1
if(e==0):
    print("-1")
else:
    for i in q:
        print(i,end=" ")