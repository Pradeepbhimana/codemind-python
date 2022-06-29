a=int(input())
b=[]
#print(a)
while(a!=0):
    b.append(a%10)
    a//=10


for i in b:
    c=0
    for j in b:
        if(i==j):
            c+=1
    if(c>=2):
        print("Not Unique Number")
        c=-1
        break
if(c!=-1):
    print("Unique Number")
    