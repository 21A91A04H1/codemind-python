n=int(input())
ar=list(map(int,input().split()))
c=0
for i in ar:
    if i%2!=0:
        c+=1
if c<=2:
    print("YES")
else:
    print("NO")