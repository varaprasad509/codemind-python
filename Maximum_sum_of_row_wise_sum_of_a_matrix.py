r,c = map(int,input().split())
mat = [list(map(int,input().split()))for i in range(r)]
l=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(mat[i][j])
    l.append(sum(a))
print(max(l))