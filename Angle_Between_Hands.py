a,b=map(int,input().split(":"))
r=abs((a*30)-(11*b)/2.0)
if(r<360-r):
    if(int(r)<r):
        print("{:.1f}".format(r))
    else:
        print("{:.1f}".format(int(r)))
else:
    if(int(360-r)<360-r):
        print("{:.1f}".format(360-r))
    else:
        print("{:.1f}".format(int(360-r)))