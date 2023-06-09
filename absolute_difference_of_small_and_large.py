s=input().split()
k=[]
for i in s:
    k.append(ord(max(i))-ord(min(i)))
print(*k)