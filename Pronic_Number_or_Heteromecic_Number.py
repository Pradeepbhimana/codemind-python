a=int(input())
for i in range(a):
    if(i*(i+1)==a):
        print("YES")
        break
else:
    print("NO")