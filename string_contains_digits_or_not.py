a=int(input())
for i in range(a):
    c=input()
    d=0
    for i in range (len(c)):
        if c[i]=="1" or c[i]=="2" or c[i]=="3" or c[i]=="4" or c[i]=="5" or c[i]=="6" or c[i]=="7" or c[i]=="8" or c[i]=="9" or c[i]=="0":
            d=d+1
        
    if d>0:
        print("Yes")
    else:
        print("No")