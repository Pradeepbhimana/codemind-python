a=int(input())
l=list(map(int,input().split()))
#mi,ma=map(int,input().split())
s=0
for i in l:
    if(i%2!=0):
        s=1
        print(False)
        break
if(s==0):
    print(True)