def fa(a):
    s=1
    while(a!=0):
        s=s*a
        a-=1
    print(s)
a=int(input())
for i in range(a):
    c=int(input())
    fa(c)