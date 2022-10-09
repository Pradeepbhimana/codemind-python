a=input()
b=a.split()
q=1000000000000000000000
for i in b:
    c=0
    for j in i:
        if(j in "aeiouAEIOU"):
            c+=1
    if(c<q):
        q=c
print(q)