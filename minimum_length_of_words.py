a=input()
c=a.split()
d=1000000000000000000
for i in c:
    if(len(i)<d):
        d=len(i)
print(d)