a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=0
    for i in c:
        for j in c:
            for k in c:
                if(i!=j and i!=k and j!=k):
                    if(i+j==k):
                        d+=1
    if(d==0):
        print("-1")
    else:
        print(d//2)
    
    