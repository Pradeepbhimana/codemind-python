a=int(input())
b=int(input())
su0=su1=0
for i in range (1,a):
    if(a%i==0):
        su0+=i
for i in range (1,b):
    if(b%i==0):
        su1+=i
        
if(su0==b and su1==a):
    print("Amicable")
else:
    print("Not Amicable")