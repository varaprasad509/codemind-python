n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in l:
    if i+k>=max(l):
        print("True",end=" ")
    else:
        print("False",end=" ")