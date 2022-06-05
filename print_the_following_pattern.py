a=int(input())
c=1
for i in range(1,a+1):
    for j in range(1,a+1):
        if(j==1 or j==a or j==c):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    c+=1