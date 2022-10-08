a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if(i not in c):
        c.append(i)
d=0
for i in c:
    if(i%2!=0):
        d+=i
print(d)