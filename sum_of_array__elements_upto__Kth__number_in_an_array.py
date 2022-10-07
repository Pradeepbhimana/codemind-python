a=int(input())
l=list(map(int,input().split()))
s=0
q=int(input())
for i in l:
    if(i==q):
        s+=i
        break
    s+=i
print(s)