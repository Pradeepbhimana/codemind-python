a=int(input())
l=list(map(int,input().split()))
w=int(input())
s=0
for i in l:
    if (i==w):
        s+=1
print(s)
       
    