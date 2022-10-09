a=input()
b=input()
d=0
c=0
for i in a:
    if(i==b):
        print(True)
        print(d)
        c=1
        break
    d+=1
if(c==0):
    print(False)
