n=int(input())
arr=list(map(int,input().split()))
c=[]
for i in arr:
    s=0
    while i:
        s=s*10+i%10
        i=i//10
    c.append(s)
for i in range(n):
    print(c[i],"",end="")