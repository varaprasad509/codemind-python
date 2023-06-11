s=input().lower().split()
l=s[1:len(s)]
d=0
m=""
for i in s[0]:
    for j in l:
        if i in j:
            d+=1
            z=j.index(i)
            q=l.index(j)
            l[q]=j[0:z]+j[z+1:]
    if len(l)==d:
        m=m+i
    d=0
if len(m)!=0:
    print(min(m))
else:
    print("-1")