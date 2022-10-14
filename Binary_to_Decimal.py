q=int(input())
for i in range(q):
    a=input()
    c=0
    d=0
    for i in a[::-1]:
        if(i=='1'):
            c+=2**d
        d+=1
    print(c)
        