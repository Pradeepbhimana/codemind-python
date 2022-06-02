a=input()
b=input()
f=0
for i in a:
    for j in b:
        if(i==j):
            f+=1
            break
    if(f==0):
        print(False)
        break
else:
    print(True)
    