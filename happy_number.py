a=int(input())
su=0
b=a
while(b!=0):
    su+=pow(b%10,2)
    b//=10
while(su//10!=0):
    b=su
    su=0
    while(b!=0):
        su+=pow(b%10,2)
        b//=10
if(su==1 or su==7):
    print("True")
else:
    print("False")