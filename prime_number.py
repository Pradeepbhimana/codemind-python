import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
a=int(input())
if(prime(a)):
    print("prime")
else:
    print("not a prime")
    