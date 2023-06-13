n=int(input())
l=list(map(int,input().split()))
m=n/2
s=[]
for i in l:
    if l.count(i)>m:
        if i not in s:
            s.append(i)
print(*s)
    