def p(a):
    b=a
    c=0
    while(b):
        c+=1
        b//=10
    b=a*a
    if(a==b%(10**c)):
        return 1
    else:
        return 0
        
a=int(input())
if(p(a)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")