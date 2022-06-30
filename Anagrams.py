a=input()
a=a.lower()
b=input()
b=b.lower()
c=0
for i in a:
    if(i not in b):
        print(False)
        c=1
        break
if(c==0):
    for i in b:
        if i not in a:
            print(False)
            c=1
            break
if(c==0):
    print(True)
    
    