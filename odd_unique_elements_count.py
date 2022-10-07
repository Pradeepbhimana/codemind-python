a=int(input())
l=list(map(int,input().split()))
b=[]
su=0
for i in l:
    if(i not in b):
        b.append(i)
for i in b:
    if(i%2!=0):
        su+=1
print(su)
    