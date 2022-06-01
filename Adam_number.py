def rev(a):
    su=0
    b=a
    while(b!=0):
        su=su*10+b%10
        b//=10
    return su
a=int(input())

if(pow(a,2))==rev(pow(rev(a),2)):
    print("True")
else:
    print("False")
    
