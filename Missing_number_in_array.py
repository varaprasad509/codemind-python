for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m=[]
    for i in range(1,n+1):
        m.append(i)
    a=[]
    b=[]
    for i in m:
        if i in l:
            a.append(i)
        else:
            b.append(i)
    if len(b)!=0:
        print(*b)
    else:
        print("0")
            