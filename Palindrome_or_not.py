a=input()
a=a.lower()
b='0'
c=0
for i in a[::-1]:
    if(c==0):
        b=i
    else:
        b+=i
    c+=1
#print(a,b)   
if(b==a):
    print(True)
else:
    print(False)