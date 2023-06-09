s=input().split()
m=[]
n=[]
for i in s:
    m.append(ord(min(i)))
    n.append(ord(max(i)))
print(sum(n)-sum(m))