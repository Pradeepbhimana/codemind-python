
a=int(input())
l=list(map(int,input().split()))
mi,ma=map(int,input().split())

q=[]
c=0
for i in range(len(l)):
    if(l[i]>=mi and l[i]<=ma):
        q.append(l[i])
        c+=l[i]
print(c)