a=input()
c=0
for i in a:
    if(i.isalnum()!=True and i!=' '):
        c+=1
print(c)