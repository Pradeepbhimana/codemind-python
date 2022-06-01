a=int(input())
b=0
d=[]
A,B=0,1
d.append(A)
d.append(B)
while(b!=a):
    c=A+B
    d.append(c)
    B=A
    A=c
    b+=1
for i in range(a):
    if(d[i]>a):
        C=d[i]
        D=d[i-1]
        break
if(abs(a-C)<abs(a-D)):
    print(C)
elif(abs(a-C)==abs(a-D)):
    print(D,C)
else:
    print(D)
    
    
    
    