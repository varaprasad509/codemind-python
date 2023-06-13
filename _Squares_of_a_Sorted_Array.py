n=int(input())
l=list(map(int,input().split()))
m=sorted(l)
a=[]
for i in range(n):
    j=m[i]*m[i]
    a.append(j)
a.sort()
print(*a)