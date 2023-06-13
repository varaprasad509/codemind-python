n=int(input())
l=map(int,input().split())
m=[]
n=[]
for i in l:
    if i not in m:
        m.append(i)
    else:
        n.append(i)
print(*n)