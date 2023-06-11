def sc(s):
    temp=""
    v="AEIOUaeiou"
    for i in s:
        if i not in v:
            temp+=i
    temp=list(temp)
    temp.sort()
    k=0
    a=[]
    for i in s:
        if i not in v:
            a.append(temp[k])
            k+=1
        else:
            a.append(i)
    m=""
    for i in a:
        m+=i
    return m
for i in input().split():
    print(sc(i),end=" ")