n=int(input())
l=list(map(int,input().split()))
even_code=0
odd_code=0
for i in l:
    if i%2==0:
        even_code+=1
    else:
        odd_code+=1
print(even_code,odd_code)