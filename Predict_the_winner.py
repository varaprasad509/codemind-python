n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(0,n):
    if i%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
m=abs(sum(even)-sum(odd))
if m%4==0:
    print("X")
else:
    print("Y")