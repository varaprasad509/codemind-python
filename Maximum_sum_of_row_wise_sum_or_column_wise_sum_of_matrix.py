r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
m=[]
n=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
        m.append(s)
for i in range(c):
    t=0
    for j in range(r):
        t+=mat[j][i]
    n.append(t)
print(max(max(m),max(n)))
    