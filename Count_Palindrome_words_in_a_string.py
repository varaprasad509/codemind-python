s=input().lower().split()
l=0
for i in s:
    n=i[::-1]
    if i==n:
        l+=1
print(l)