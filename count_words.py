a=input()
a=a.lower()
w=a.split(" ")
ab=['a','e','i','o','u']
af=0
for i in w:
    d=0
    for j in i:
        
        if(d==0):
            c=j
        else:
            e=j
        d+=1
    if(c in ab and e not in ab):
        af+=1
print(af)