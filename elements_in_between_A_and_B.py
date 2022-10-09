a=int(input())
l=list(map(int,input().split()))
mi,ma=map(int,input().split())
f=0
for i in l:
    if(i>=mi and i<=ma):
        print(i,end=" ")
        f=1
if(f==0):
    print("-1")