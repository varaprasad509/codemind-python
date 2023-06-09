n=input().lower().split()
n="".join(n)
s=sorted(n)
c=[]
for i in s:
    if s.count(i)==1:
        c.append(i)
for i in c:
    print(i,end="")