n=int(input())
a=list(map(int,input().split()))
sum=1
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i==j:
            continue
        else:
            sum=sum*a[j]
    print(sum,end=" ")
    sum=1