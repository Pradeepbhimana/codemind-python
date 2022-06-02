def p(a):
    b='q'
    c=0
    for i in a[::-1]:
        if(c==0) :
           b=i
        else:
            b+=i
        c+=1
    if(b==a):
        return 1
    else:
        return 0
       
         
a=input()
a=a.lower()
b=a.split(" ")
c=0
for i in b:
    if(p(i)):
        #print(i)
        c+=1
print(c)
        
