a,b=map(int,input().split())
l=list(map(int,input().split()))
su=0
d=0
for i in range(a):
    su=0
    for j in range(i,a):
        su+=l[j]
        if(su==b):
            d+=1
            break
print(d)