a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if(i not in c):
        c.append(i)
e=0
for i in c:
    d=0
    for j in b:
        if(i==j):
            d+=1
    if(d==i):
        e+=1
print(e)
    