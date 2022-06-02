a=int(input())
b=map(int,input().split())
so=0
for i in b:
    so=so*10+i
so+=1
d=[]
while ( so!=0):
    d.append(so%10)
    so//=10
for i in d[::-1]:
    print(i,end=" ")

    