a=int(input())
b=[]
while(a):
    b.append(a%10)
    a//=10
print(max(b))