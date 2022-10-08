a=int(input())
l=list(map(int,input().split()))
w=0

for i in l:
    if(i==0 or i==1):
        pass
    else:
        print(False)
        w=1
        break
if(w==0):
    print(True)
         