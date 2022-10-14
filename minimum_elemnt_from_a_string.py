a=input()
b=a.split(" ")
c=b[-1]
q=min(c)
if(q.lower()!=q):
    if(q.lower() in c):
        print(q.lower())
    else:
        print(q)
else:
    print(q)