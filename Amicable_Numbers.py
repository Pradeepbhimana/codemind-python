a=int(input())
b=int(input())
s=0
for i in range(1,a):
    if(a%i==0):
        s+=i
if(s==b):
    s=0
    for i in range(1,b):
        if(b%i==0):
            s+=i
    if(s==a):
        print("Amicable")
    else:
        print("Not Amicable")
else:
    print("Not Amicable")