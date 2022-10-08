a=int(input())
l=list(map(int,input().split()))
w=0
for i in range(1,a-1):
    if(l[i]%2!=0):
        if(l[i-1]%2==0 and l[i+1]%2==0):
            w+=1
print(w)