a=int(input())
b=a
c=0
while(b!=0):
    c+=1
    b//=10
d=[]
b1=a
for i in range(c):
    d.append(b1%10)
    b1//=10
q=0
for i in d:
    if(i>q):
        q=i
print(q)