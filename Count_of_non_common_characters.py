m=input().lower().split()
n=input().lower().split()
s1="".join(m)
s2="".join(n)
c=[]
for i in s1:
    if i not in s2:
        if i not in c:
            c.append(i)
for i in s2:
    if i not in s1:
        if i not in c:
            c.append(i)
print(len(c))