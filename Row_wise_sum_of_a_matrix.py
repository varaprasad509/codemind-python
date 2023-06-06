r,c = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(r)]
for i in arr:
    print(sum(i),end=" ")