n=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
m=[]
for i in range(len(A)):
    c=A[i]+B[i]
    m.append(c)
print(*m)