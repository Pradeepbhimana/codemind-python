#include<stdio.h>
#include<string.h>

    
a=input()
b=len(a);
#printf("%d",b);
for i in range (b):
    if(a[i]=='0'):
        if(i==0):
            print("0",end="")
            
        
        else:
            print("000",end="")
        
    
    elif(a[i]=='1'):
        if(i==0):
            print("1",end="")
        
        else:
            print("001",end="")
        
    
    elif(a[i]=='2'):
        if(i==0):
            print("10",end="")
        
        else:
            print("010",end="")
        
    
    elif(a[i]=='3'):
        if(i==0):
            print("11",end="")
        
        else:
            print("011",end="")
        
    
    elif(a[i]=='4'):
        print("100",end="")
    
    elif(a[i]=='5'):
        print("101",end="")
    
    elif(a[i]=='6'):
        print("110",end="")
    
    elif(a[i]=='7'):
        print("111",end="")
    
    
