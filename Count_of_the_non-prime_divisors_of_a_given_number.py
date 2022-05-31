def prime(a):
    if(a<=1):
        return 0
    else:
        for i in range (2,a):
            if(a%i==0):
                break
        else:
            return 1
a=int(input())
c=0
for i in range (1,a):
    if(a%i==0 and prime(i)!=1):
        c+=1
print(c+1)
        
    