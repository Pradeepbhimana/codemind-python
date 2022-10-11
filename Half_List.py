a=int(input())
#print(a)
l=list(map(int,input().split()))
b=[]
for i in range(a-1,(a//2)-1,-1):
    b.append(l[i])


for i in range(a):
    if(l[i]not in b):
        b.append(l[i])
for i in b:
    print(i,end=" ")