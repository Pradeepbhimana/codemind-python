a=int(input())
l=list(map(int,input().split()))
b=[]
b1=0
q,p=map(int,input().split())

for i in l:
    if(i<q or i>p):
        b.append(i)
        b1=1
if(b1==0):
    print("-1")
else:
    for i in b:
        print(i,end=" ")
        
    