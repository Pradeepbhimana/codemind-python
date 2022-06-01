w=input()
b=n=l=a=o=0
for i in w:
    if(i=='b'):
        b+=1
    elif(i=='l'):
        l+=1
    elif(i=='o'):
        o+=1
    elif(i=='n'):
        
        n+=1
    elif(i=='a'):
        a+=1
    
q=0
while(b>=1 and o>=2 and a>=1 and l>=2 and n>=1):
    q+=1
    b-=1
    o-=2
    a-=1
    l-=2
    n-=1
print(q)