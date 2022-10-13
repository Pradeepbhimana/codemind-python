q=int(input())
for i in range(q):
    a=input()
    c=0
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            a.replace(a[i],"")
            c+=1
            
            i-=1
    print(c)