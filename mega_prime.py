def pr(a):
    if(a<=1):
        return 0
    else:
        for i in range(2,a):
            if(a%i==0):
                return 0
        else:
            return 1
def mg(a):
    while(a!=0):
        if(pr(a%10)!=1):
            return 0
            break
        a//=10
    else:
        return 1
        
    
a=int(input())
if(pr(a)):
    if(mg(a)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")

   