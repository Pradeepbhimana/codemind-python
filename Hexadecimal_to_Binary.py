a=int(input())
b="0000"
c="0001"
d="0010"
e="0011"
f="0100"
g="0101"
h="0110"
i="0111"
j="1000"
k="1001"
l="1010"
s="1011"
n="1100"
o="1101"
p="1110"
q="1111"
for i in range(a):
    x=input()
    m=""
    for i in range(len(x)):
        if x[i]=="0":
            m+=b
        elif x[i]=="1":
            m+=c
        elif x[i]=="2":
            m+=d
        elif x[i]=="3":
            m+=(e)
        elif x[i]=="4":
            m+=f
        elif x[i]=="5":
            m+=(g)
        elif x[i]=="6":
            m+=(h)
        elif x[i]=="7":
            m+=(i)
        elif x[i]=="8":
            m+=(j)
        elif x[i]=="9":
            m+=(k)
        elif x[i]=="A":
            m+=(l)
        elif x[i]=="B":
            m+=(s)
        elif x[i]=="C":
            m+=(n)
        elif x[i]=="D":
            m+=(o)
        elif x[i]=="E":
            m+=(p)
        elif x[i]=="F":
            m+=(q)
    print(m)