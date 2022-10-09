a=input()
b=a.split()
q=0
for i in b:
    c=0
    for j in i:
        if(j in "aeiouAEIOU"):
            c+=1
    if(c>q):
        q=c
d=0
for i in b:
    c=0
    for j in i:
        if(j in "aeiouAEIOU"):
            c+=1
    if(c==q):
        d+=1
print(d)