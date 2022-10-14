q=int(input())
for i in range(q):
    
    a=int(input())
    b=[]
    while(a):
        b.append(a%2)
        a//=2
    for i in b[::-1]:
        print(i,end="")
    print()