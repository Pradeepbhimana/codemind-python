a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c1=[]
c2=[]
for i in l1:
    if(i not in c1):
        c1.append(i)
l1=c1

for i in l2:
    if(i not in c2):
        c2.append(i)
l2=c2
d=0
for i in l1:
    if(i not in l2):
        d+=1
for i in l2:
    if i not in l1:
        d+=1
print(d)     