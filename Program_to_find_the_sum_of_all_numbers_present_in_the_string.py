s=input()
ans = 0
for i in s:
    if i >= '0' and i<= '9':
        ans = ans+ord(i)-48
print(ans)