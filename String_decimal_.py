q=int(input())
for j in range (q):
    a=input()
    b=len(a)
    c=0
    for i in a:
        if(i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='0'):
            c+=1
        
    if(c==0):
        print(True)
    else:
        print(False)