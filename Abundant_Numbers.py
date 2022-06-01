def kk(a):
    su=0
    if(a<=1):
        return 0
    else:
        for i in range(1,a):
            if(a%i==0):
                su+=i
    if(su>a):
        return 1
    else:
        return 0
a=int(input())
if(kk(a)):
    print("True")
else:
    print("False")