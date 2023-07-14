def reverse(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input())
rev=0
if n<0:
    rev=1
n=abs(n)
n=reverse(n)
if rev==1:
    print(-n)
else:
    print(n)