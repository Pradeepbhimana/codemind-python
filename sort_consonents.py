b=input()

q='aeiouAEIOU'
w=b.split(" ")
for i in w:
    a=list(i)
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i] not in q and a[j] not in q and a[i]!=' ' and a[j]!=' '):
                if(a[i]<a[j]):
                    te=a[i]
                    ce=a[j]
                    a[i]=ce
                    a[j]=te
             
    b=str(a)
    
    print("".join(a),end=" ")