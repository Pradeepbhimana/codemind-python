a=input()
b=a.split()
for i in b:
    c=0
    for j in i:
        if(j in "aeiouAEIOU"):
            c+=1
    print(c,end=" ")