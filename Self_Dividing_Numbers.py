def sel(a):
    b=a
    while(a!=0):
        if(a%10==0):
            return 0
        else:
            if(b%(a%10)!=0):
                return 0
                break
        a//=10
    else:
        return 1
            
    
    
    
    
    
    
    
a=int(input())

b=int(input())
for i in range(a,b+1):
    if(sel(i)):
        print(i,end =" ")