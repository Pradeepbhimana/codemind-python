a=input()
c=a.split()
d=0
for i in c:
    for j in i[::-1]:
        print(j,end="")
    print(end=" ")