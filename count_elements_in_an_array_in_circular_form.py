a=int(input())
l=list(map(int,input().split()))
#mi,ma=map(int,input().split())
s=0
for i in range(1,a-1):
    if(l[i-1]%2==0 and l[i+1]%2!=0 or l[i-1]%2!=0 and l[i+1]%2==0  ):
        s+=1
if(l[a-2]%2==0 and l[0]%2!=0 or l[a-2]%2!=0 and l[0]%2==0  ):
    s+=1
if(l[a-1]%2==0 and l[1]%2!=0 or l[a-1]%2!=0 and l[1]%2==0 ):
    s+=1
print(s)
    