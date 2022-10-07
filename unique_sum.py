a=int(input())
l=list(map(int,input().split()))
b=[]
su=0
for i in l:
    if(i not in b):
        b.append(i)
for i in b:
   su+=i
print(su) 

        