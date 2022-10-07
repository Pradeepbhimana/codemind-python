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
c=0
q=0
for i in l:
    if(pr(i)):
        c+=i
        q+=1
   
   
#print("{:.2f}".format(c/q))
print(q)
            
            
            