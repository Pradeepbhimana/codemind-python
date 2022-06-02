
a=input()
Q=a.split(" ")
for i in Q:
    b=ord(min(i))
            
    c=ord(max(i))
    print(abs(b-c),end=" ")
    
    