a=int(input())
for i in range(a):
    b=int(input())
    l=list(map(int,input().split()))
    for i in range(1,b+1):
        if(i not in l):
            print(i)
            break