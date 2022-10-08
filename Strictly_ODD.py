a=int(input())
l=list(map(int,input().split()))
w=0
for i in range(a):
    if(i%2==0):
        if(l[i]%2!=0):
            print(False)
            w=1
            break
    #if(i%2!=0):
     #   if(l[i]%2==0):
      #      print
if(w==0):
    print(True)
    