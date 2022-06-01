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
for i in range (c):
    for j in range (c):
        if(i!=j):
            if(d[i]==d[j]):
                q+=1
                break
    if(q>0):
        print("Not Unique Number")         
        break
        

                
            

else:
    print("Unique Number")
    