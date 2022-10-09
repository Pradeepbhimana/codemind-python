a=input()
b=a.split()
for i in range(len(b)):
    if(i%2==0):
        for j in b[i][::-1]:
            print(j,end="")
        print(end=" ")
    else:
        for j in b[i]:
            print(j,end="")
        print(end=" ")
    
    