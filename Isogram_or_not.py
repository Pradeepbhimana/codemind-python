a=input()
fla=0
for i in range (len(a)):
    for j in range (len(a)):
        if(i!=j and a[i]!=' '):
            if(a[i]==a[j]):
                fla=1
                break
    if(fla==1):
        print(False)
        break
else:
    print(True)
        