a=int(input())
c=[]
while(a):
    c.append(a%10)
    a//=10
#print(c)
for i in range(len(c)-1,-1,-1):
    if(c[i]==6):
        c[i]=9
        break
for i in c[::-1]:
    print(i,end="")
    