def feb(a):
    c=0
    a1=0
    a2=1
    print(a1,end=" ")
    print(a2,end=" ")
    while(c<a-2):
        a3=a1+a2
        print(a3,end=" ")
        a1=a2
        a2=a3
        c+=1
        
a=int(input())
feb(a)