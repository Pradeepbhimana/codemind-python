import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
a=int(input())
c=0
for i in range(1,a+1):
    if(a%i==0):
        if(prime(i)==0):
            c+=1
print(c+1)
    