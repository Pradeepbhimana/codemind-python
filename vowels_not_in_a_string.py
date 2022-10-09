a=input()
a=a.lower()
b="aeiou"
c=0
for i in b:
    if(i not in a):
        c=1
        print(i,end=" ")
if(c==0):
    print("0")