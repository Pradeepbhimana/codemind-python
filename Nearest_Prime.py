import  math
def pr(a):
    for i in range (2,a):
        if(a%i==0):
            return 0
    else:
        return 1
def lp(a):
    while (pr(a)!=1) :
        a-=1
    return a
def hp(a):
    while(pr(a)!=1):
        a+=1;
        
    return a
b=int(input())
for i in range (b):
        
    a=int (input());
    c=lp(a)
    d=hp(a)
    if(abs(c-a)<abs(a-d) or abs(c-a)==abs(a-d)):
        print(c)
    else:
        print(d)