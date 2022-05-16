import  math
def pr(a):
    if a==0 or a==1:
        return 0
    else:
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

        
a=int (input());
c=lp(a)
d=hp(a)
q=0
if(pr(a)==1):
    print(q)
else:
    if(abs(c-a)<abs(a-d) or abs(c-a)==abs(a-d)):
        print(abs(c-a))
    else:
        print(abs(a-d))