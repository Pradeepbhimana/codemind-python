a=input()
c=a.split()
d=0
for i in c:
    if(len(i)>d):
        d=len(i)
print(d)