def sq(a):
    if(a<=1):
        return 1
    else:
        for i in range (a):
            if(i*i==a):
                return 1
                break
        else:
            return 0
a=int(input())
b=list(map(int,input().split()))
su=0
for i in b:
    if(sq(i)):
        su+=i
print(su)
#print(sq(1))