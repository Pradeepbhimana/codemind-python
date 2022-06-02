
a=input()
b='z'
for i in a:
    if(b>i and i!=' '):
        b=i
        
c=max(a)
mi=ma=0
for i in a:
    if(i==b):
        mi+=1
    if(i==c):
        ma+=1
print(b,mi,c,ma)
    
    