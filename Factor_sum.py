def fac(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
a=list(map(int,input().split(',')))
m=[]
for i in a:
    if fac(i) in a:
        m.append(i)
m.sort()
if len(m)==0:
    print('-1')
else:
    print(*m)
            