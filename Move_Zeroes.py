n=int(input())
l=list(map(int,input().split()))
zeroes=[]
num=[]
for i in l:
    if i==0:
        zeroes.append(i)
    else:
        num.append(i)
for i in zeroes:
    num.append(i)
print(*num)
    