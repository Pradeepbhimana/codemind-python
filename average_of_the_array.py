
a=int(input())
l=list(map(int,input().split()))
w=0
for i in l:
    w+=i
s=w/a
print("{:.2f}".format(s))