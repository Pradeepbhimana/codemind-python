a=input()
for i in a:
    c=ord(i)-48
    if(c%2!=0):
        print(c*c,end="")