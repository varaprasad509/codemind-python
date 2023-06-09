n=input().lower().split()
n="".join(n)
a=sorted(n)
c=[]
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    print(i,end="")