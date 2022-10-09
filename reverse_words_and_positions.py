a=input()
b=a.split()
for i in b[::-1]:
    for j in i[::-1]:
        print(j,end="")
    print(end=" ")