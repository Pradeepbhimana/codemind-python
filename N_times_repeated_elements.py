a=int(input())
l=list(map(int,input().split()))
b=[]
b1=0
q=int(input())
q1=[]
for i in l:
    if(i not in b):
        b.append(i)
for i in b:
    c=0
    for j in l:
        if(i==j):
            c+=1
    if(c==q):
        q1.append(i)
        b1=1
if(b1==0):
    print("-1")
else:
    for i in q1:
        print(i,end=" ")
        
    