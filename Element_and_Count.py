a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if(i not in b):
        b.append(i)
for i in b:
    c=0
    for j in l:
        if(i==j):
            c+=1
    print(i,c,end=" ")