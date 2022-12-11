def prime(m):
    c=0
    if m==1:
        return False
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            c=1
            break
    if c==0:
        return True
    else:
        return False
n=int(input())
m=int(input())
c1=0
for i in range(n,m+1):
    if prime(i):
        c1+=1
print(c1)

