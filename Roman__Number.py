n=int(input())
a=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
b=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
i=12
while n:
    x=n//a[i]
    n=n%a[i]
    while x:
        print(b[i],end="")
        x-=1
    i-=1