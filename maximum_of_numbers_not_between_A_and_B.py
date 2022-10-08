a=int(input())
l=list(map(int,input().split()))
mi,ma=map(int,input().split())
q=0
e=0
for i in l:
    if(i<mi or i>ma):
        if(i>q):
            e=1
            q=i
if(e==0):
    print("-1")
else:
    print(q)
        

