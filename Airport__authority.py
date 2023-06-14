c=[]
n=int(input())
for i in range(n):
    a=int(input())
    c.append(a)
threshold_weight=int(input())
double_pay=0
pay=0
for i in c:
    if i>threshold_weight:
        double_pay+=1
    else:
        pay+=1
print(2*double_pay+pay)