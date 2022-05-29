a=input()
w = a.split(" ")
d=" "
for i in w[::-1]:
    for j in i[::-1]:
        print(j,end="")
        
    print(end=" ")

