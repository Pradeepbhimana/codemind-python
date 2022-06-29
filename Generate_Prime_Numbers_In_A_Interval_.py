def pr(a):
    if(a<=1):
        return 0
    else:
        for i in range(2,a):
            if(a%i==0):
                return 0
                break
        else:
            return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(pr(i)):
        print(i)