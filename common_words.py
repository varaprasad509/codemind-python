s1=input().lower().split()
s2=input().lower().split()
c=[]
for i in s2:
    if i in s1:
        c.append(i)
print(*c)