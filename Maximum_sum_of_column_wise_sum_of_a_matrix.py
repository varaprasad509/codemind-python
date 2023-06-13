n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
k=[]
for i in range(m):
    s=0
    for j in range(n):
        s+=mat[j][i]
    k.append(s)
print(max(*k))