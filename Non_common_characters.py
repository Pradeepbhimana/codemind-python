s=input()
p=input()
s=s.lower()
p=p.lower()

d=""
c=0
for i in p:
    if i not in s and i.isalpha() and i not in d :
        d+=i
        c+=1
for i in s:
    if i not in p and i.isalpha() and i not in d :
        d+=i
        c+=1

print(c)