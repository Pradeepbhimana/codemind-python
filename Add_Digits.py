def s(a):
    s=0
    while(a):
        s+=a%10
        a//=10
    return s
a=int(input())
b=s(a)
while(b//10!=0):
    b=s(b)
print(b)
        
        