import math
def rev(a):
    s=0
    while(a):
        s=s*10+a%10
        a//=10
    return s
a=int(input())

if((pow((a),2))==rev(pow(rev(a),2))):
    print(True)
else:
    print(False)
