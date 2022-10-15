a=input()
a=a.lower()
b=input()
b=b.lower()
a=a.split()
b=b.split()
c=[]
for i in a:
    
    if(i  not in c ):
        c.append(i)
d=0
for  i in c:
    
    if( i in b):
        #print(i)

        d+=1
print(d)







