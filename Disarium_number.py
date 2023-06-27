n=int(input())
c=0
m=n
p=0
x=m
while n>=1:
    c+=1
    n=n/10
while m>=1:
    r=m%10
    p=pow(r,c)+(p)
    c-=1
    m=m//10
if p==x:
    print("True")
else:
    print("False")