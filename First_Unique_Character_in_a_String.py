a=input()

for i in range (len(a)):
    c=0
    for j in range (len(a)):
        if(i!=j):
            if(a[i]==a[j] and a[i]!=' '):
                c=1
    if(c==0):
        print(i)
        break
if(c==1):
    print("-1")
            
                