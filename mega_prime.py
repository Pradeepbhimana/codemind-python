c=int(input())
for i in range (2,c//2+1):
    if(c%i==0):
        print("Not Mega Prime")
        break
    
else:
    d=c
    while(d!=0):
        e=d%10
        if(e==2 or e==3 or e==5 or e==7 ):
            d=d//10;
        else:
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
