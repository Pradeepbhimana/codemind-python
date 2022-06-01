a=int(input())
b,c=a,0
while(b!=0):
    c+=1
    b//=10
d=a*a
#print(d%pow(10,c))
if(a==d%pow(10,c)):
     print("Automorphic Number")
else:
    print("Not an Automorphic Number")