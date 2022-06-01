a=int(input())
for i in range (a):
    b,c=map(int,input().split())
    d=0
    for j in range (b,c+1):
        if(j%10==2 or j%10==3 or j%10==9):
            d+=1
    print(d)
    