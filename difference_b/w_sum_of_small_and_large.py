
a=input()
Q=a.split(" ")
ma=mi=0
for i in Q:
    mi+=ord(min(i))
            
    ma+=ord(max(i))
print(abs(mi-ma))
    
    