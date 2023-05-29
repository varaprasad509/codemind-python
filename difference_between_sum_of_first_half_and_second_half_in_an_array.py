n=int(input())
a=list(map(int,input().split()))
f=a[:n//2]
s=a[n//2:]
print(abs(sum(f)-sum(s)))