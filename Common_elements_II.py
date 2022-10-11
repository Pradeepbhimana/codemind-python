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
c3=[]
for i in l1:
    if(i not in l2):
        c3.append(i)
for i in l2:
    if i not in l1:
        c3.append(i)
for i in c3:
    print(i,end=" ")