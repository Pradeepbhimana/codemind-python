b=input()
a=list(b)
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i].isalnum()==True and a[j].isalnum()==True):
            if(a[i]<a[j]):
                te=a[i]
                ce=a[j]
                a[i]=ce
                a[j]=te
         
b=str(a)

print("".join(a))