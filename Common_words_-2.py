a=input()
a=a.lower()
b=input()
b=b.lower()
a=a.split()
b=b.split()
c=[]
d=0
for i in a:
   for j in b:
       if(a.count(i)==1 and b.count(j)==1 and i==j):
           d+=1
print(d)
   