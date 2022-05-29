a=input()
a=a.lower()

ab=['a','e','i','o','u']
af=0
d=0
for i in a[::-1]:
    
    if(i in ab and a[d] not in ab and i!=' ' and a[d]!=' ' or i not in ab and a[d] in ab and i!=' ' and a[d]!=' '):
        af+=1
        #print(i ,"i"," ",a[d]," d")
    if(d==(len(a)//2)-1):
       break 
    d+=1
#print(a)
print(af)