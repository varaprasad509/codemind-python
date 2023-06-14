m=input().lower().split()
n=input().lower().split()
s1="".join(m)
s2="".join(n)
c=[]
for i in s1:
    if i in s2:
        if i not in c:
            c.append(i)
c.sort()
if len(c)!=0:
    for i in c:
        print(i,end="")
else:
    print("-1")