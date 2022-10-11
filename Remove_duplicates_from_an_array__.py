a=int(input())
#print(a)
l=list(map(int,input().split()))
b=[]
for i in l:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,end=" ")