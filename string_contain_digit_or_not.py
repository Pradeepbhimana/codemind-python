

a=input()
b=len(a)
c=0
for i in a:
    if(i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
        c+=1
if(c==0):
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")