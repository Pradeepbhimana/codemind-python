
import math
def rev(a):
    s=0
    while(a):
        s=s*10+a%10
        a//=10
    return s
a=int(input())
b=a
c=1
s=0
a=rev(a)
while(a):
    s=s+pow((a%10),c)
    c+=1
    a//=10
if(s==b):
    print(True)
else:
    print(False)
    
    
#print(pow(12,2))