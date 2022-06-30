
a=input()
a=a.lower()
w=a.split(" ")
c=0
q="aeiou"
for j in w:
    if(j[0] in q and j[-1] not in q):
        c+=1
print(c)
   