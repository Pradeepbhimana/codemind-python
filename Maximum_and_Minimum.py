a=int(input())
l=list(map(int,input().split()))
b=list(set(l))
q=[]
for i in b:
    c=0
    for j in l:
        if(i==j):
            c+=1
    if(c==i):
        q.append(i)
if(len(q)==0):
    print(-1)
else:
    print(min(q),max(q))