a=int(input())
l=list(map(int,input().split()))
#mi,ma=map(int,input().split())
q=100000000000000000000000000
e=0
for i in l:
    e+=i
q=e//a
e=0
for i in l:
    if(i<=q):
        e+=1
print(e)