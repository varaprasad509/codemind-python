n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)!=1:
        c.append(i)
for i in c:
    if c.count(i)%2!=0:
        c.remove(i)
print(len(c)//2)