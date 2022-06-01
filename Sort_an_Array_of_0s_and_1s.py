a=int(input())
b=list(map(int,input().split()))
b.sort()
for i in range (a):
    print(b[i],end=" ")