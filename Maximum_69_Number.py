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
for i in range (c-1,-1,-1):
    if(d[i]==6):
        d[i]=9
        break
sum=0
for i in d[::-1]:
    if(i==0):
        sum=sum*10+10
    else:
        sum=sum*10+i
print(sum)