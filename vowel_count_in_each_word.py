n=input()
s=n.split()
for i in s:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    print(c,end=' ')