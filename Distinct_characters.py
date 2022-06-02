def sort(lst):
      
    return sorted(lst, key = lambda x: (isinstance(x, str), x))
a=input()
a=a.lower()
d=0
b=[]
for i in a:
    c=0
    for j in a:
        if(i==j and i!=' '):
            c+=1
    if(c==1):
        b.append(i)
        #print(i)
        d+=1
b=sort(b)
for i in b:
    print(i,end="")