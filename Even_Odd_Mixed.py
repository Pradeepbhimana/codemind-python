a=int(input())
b=a
e=0
o=0
while(b!=0):
    c=b%10
    if(c%2==0):
        e+=1
    else:
        
        o+=1
    b//=10
if(e==0):
    print("Odd")
elif(o==0):
    print("Even")
else:
    print("Mixed")
    