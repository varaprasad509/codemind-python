n=input().lower().split()
n="".join(n)
s=sorted(n)
c=[]
for i in s:
    if i not in c:
        c.append(i)
print(len(c))