a=int(input())
l=list(map(int,input().split()))
w=int(input())
s=0
for i in l:
    if i==w:
        print(True)
        s=1
        break
if(s==0):
    print(False)ac