a=input()
a=a.lower()
a=a.split()
b=a[0]
d=0
for i in b:
    c=0
    for j in a:
        if(i in j):
            c+=1
    if(c==len(a)):
        d+=1
print(d)
    