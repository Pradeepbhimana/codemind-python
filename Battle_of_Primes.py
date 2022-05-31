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
a=int(input())
b=int(input())
c=a+b+1
while(pr(c)!=1):
    c+=1
print(c-(a+b))
    