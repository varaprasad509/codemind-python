n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(0,n,2):
    even.append(l[i])
for i in range(1,n,2):
    odd.append(l[i])
if(sum(even)-sum(odd))==0:
    print("YES")
else:
    print("NO")