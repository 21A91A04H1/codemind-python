n,m=map(int,input().split())
z=n+m*2
if n==0 and m%2==0:
    print("YES")
elif n==0 and m%2!=0:
    print("NO")
elif z%2==0:
    print("YES")
else:
    print("NO")