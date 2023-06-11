n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(len(l)):
    p.append(len(str(l[i])))
maxi=max(p)
m=[]
for i in l:
    if len(str(i))==maxi:
        m.append(i)
print(*m)