q=int(input())
for j in range(q):
    a=input()
    a=a[::-1]
    d=0
    c=0
    for i in a:
        if(i=="1"):
            
            c+=2**d
        d+=1
    b=[]
    while(c):
        b.append(c%8)
        c//=8
    for i in b[::-1]:
        print(i,end="")
    print()
        
        