a=input()
a=a.lower()
c=0

if('a' not in a ):
    print("a",end=' ')
else:
    c+=1
if('e' not in a ):
    print("e",end=' ')
else:
    c+=1
    
if('i' not in a ):
    print("i",end=' ')
else:
    c+=1

if('o' not in a ):
    print("o",end=' ')
else:
    c+=1

if('u' not in a ):
    print("u",end=' ')
else:
    c+=1
if(c==5):
    print("0")
