a=int(input())
d=[]
for i in range (a):
    c=int(input())
    d.append(c)
b=int(input())
s=0
for i in d:
    if(i>b):
        s+=2
    else:
        s+=1
print(s)