
a=input()
a=a.lower()
b='aeiou'
c=0
for i in a:
    if( i in b):
        c+=1
print(c)