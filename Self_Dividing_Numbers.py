def sf(a):
    b=a
    while(b!=0):
        c=b%10
        #print(c)

        if (c==0  or a%c!=0 ):
            return 0
            
        
        b=b//10
        #print("b ",b)
    else:
        return 1
        
        
        
        
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(sf(i)):
        print(i,end=" ")
