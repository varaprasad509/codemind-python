n=int(input())
l=list(set(map(int,input().split())))
if len(l)>=3:
    f=max(l)
    l.remove(f)
    s=max(l)
    l.remove(s)
    t=max(l)
    print(t)
elif len(l)<3:
    f=max(l)
    print(f)
else:
    print(max(l))