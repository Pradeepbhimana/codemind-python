a=input()
a=a.lower()
b=""

d=1
for i in a:
    if(i not in b and i!=' '):
        b+=i
print(len(b))
    



    
    