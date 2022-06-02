
a=input()
b=a.split()
c=0

for i in b:
    if(c==0):
        print(min(i),end=" ")
    if(c==len(b)-1):
        
        print(max(i),end=" ")
    c+=1