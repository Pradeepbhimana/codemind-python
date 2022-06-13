s=input()
p=input()
s=s.lower()
p=p.lower()
s=s.split(" ")
p=p.split(" ")
d=[]
for i in p:
    if i in s and i.isalpha() :
        d.append(i)
for i in d:
    print (i,end=" " )