s=input()
p=input()
s=s.lower()
p=p.lower()

d=""
for i in p:
    if i not in s and i.isalpha() and i not in d :
        d+=i
for i in s:
    if i not in p and i.isalpha() and i not in d :
        d+=i
d=sorted(d)

print(len(d))