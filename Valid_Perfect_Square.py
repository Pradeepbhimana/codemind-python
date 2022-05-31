a=int(input())
c=0
for i in range (a):
    b=int(input())
    if(b==0):
        print("True")
    else:
        
        for j in range (1,b):
            if(b==j*j):
                c=1
                break
        if(c==1):
            print("True")
        else:
            print("False")
        c=0
    