def pr(a):
    if(a<=1):
        return 0
    else:
        for i in range (2,a):
            if(a%i==0):
                return 0
                break
        else:
            return 1
d=[]

a=int(input())
for i in range (a):
    if(pr(i)):
        d.append(i)
c=0
for i in d:
    for j in d:
        if(i!=j):
            if(i*j==a):
                c+=1
                print(i,j)
                break
    if(c>0):
        break
    
if(c==0):
    print("-1")

        
    
