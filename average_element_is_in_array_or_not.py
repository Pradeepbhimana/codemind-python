
a=int(input())
l=list(map(int,input().split()))
w=0
for i in l:
    w+=i
s=w//a
p=0
for i in l:
    if i ==s:
        print(True)
        p=1
        break
if(p==0):
    print(False)
    