a=input()
a=a.lower()
d=0
for i in a:
    c=0
    for j in a:
        if(i==j and i!=' '):
            c+=1
    if(c==1):
        #print(i)
        d+=1
print(d)