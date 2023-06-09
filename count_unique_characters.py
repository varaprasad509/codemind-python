n=input().lower().split()
n="".join(n)
c=[]
for i in n:
    if n.count(i)==1:
        c.append(i)
print(len(c))
    