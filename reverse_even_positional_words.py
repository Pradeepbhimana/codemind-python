a=input()
w = a.split(" ")
d=0
for i in w:
    if(d%2==0):
        for j in i[::-1]:
            print(j,end="")
            
        print(end=" ")
    else:
        print(i,end=" ")
    d+=1

