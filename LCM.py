def lcm(a,b):
    for i in range (1,1001):
        for j in range (1,1001):
            if a*i==b*j:
                return(a*i)
                break
a,b=map(int,input().split())
print(lcm(a,b))

