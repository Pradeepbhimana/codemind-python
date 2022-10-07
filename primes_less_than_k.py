def pr(a):
    if(a>=2):
        for i in range(2,int(a**0.5)+1):
            if(a%i==0):
                return 0
        return 1
    else:
        return 0
a=int(input())
l=list(map(int,input().split()))
c=int(input())
q=0
for i in l:
    if(pr(i)):
        #print(i)
        if(i<=c):
         #   print(">",i)
            q+=1
print(q)
            
            
            