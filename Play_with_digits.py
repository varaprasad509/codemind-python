n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    while i:
        c=c+i%10
        i=i//10
print(c)