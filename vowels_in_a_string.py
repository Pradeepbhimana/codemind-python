a=input()
b=input()
c=0
for i in range(len(a)):
    if(a[i]==b):
        print(True)
        print(i)
        c+=1
        break
if(c==0):
    print(False)