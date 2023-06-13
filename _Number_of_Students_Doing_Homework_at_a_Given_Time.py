n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
c=0
m=int(input())
for i in range(n):
    if l[i]<=m<=l1[i]:
        c+=1
print(c)