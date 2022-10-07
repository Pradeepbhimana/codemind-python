a=int(input())
l=list(map(int,input().split()))
b=[]
b1=0
q,p=map(int,input().split())

for i in l:
    if(i<q or i>p):
        
        b1+=i
print(b1)