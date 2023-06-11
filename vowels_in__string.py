n=input()
l=[]
for i in n:
    if i in 'aeiouAEIOU':
        if i not in l:
            l.append(i)
if len(l)==0:
    print(-1)
else:
    print(*l)