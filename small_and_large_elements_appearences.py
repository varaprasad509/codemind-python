s=input().split()
b=""
for i in s:
    b=i+b
print(min(b),b.count(min(b)),max(b),b.count(max(b)),end=" ")