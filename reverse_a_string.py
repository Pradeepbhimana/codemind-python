a=input()
c=a.split()
d=0
for i in c[::-1]:
    for j in i[::-1]:
        print(j,end="")
    print(end=" ")