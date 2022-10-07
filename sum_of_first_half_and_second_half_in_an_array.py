a=int(input())
l=list(map(int,input().split()))
s=0
q=a//2
for i in range(q+1):
    #print(i,end=" ")
    s+=i
print(s)
#print()
s=0
for i in range(q+1,len(l)+1):
    s+=i
    #print(i,end=" ")
print(s)