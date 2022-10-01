def solve():
    l = input()
    xa, ya = [int(s) for s in input().split(" ")]
    xb, yb = [int(s) for s in input().split(" ")]
    xf, yf = [int(s) for s in input().split(" ")]
    xdiff = abs(xa-xb)
    ydiff = abs(ya-yb)
    ans = xdiff + ydiff
    if xdiff != 0 and ydiff!=0:
        print(ans)
        return
    if xdiff == 0:
        if ya > yb:
            ya, yb = yb, ya
        if ya <= yf and yf <= yb and xa == xf:
            ans += 2
            print(ans)
        else:
            print(ans)
    else:
        if xa > xb:
            xa, xb = xb, xa
        if xa <= xf and xf <= xb and ya == yf:
            ans += 2
            print(ans)
        else:
            print(ans)

t = int(input())
for _ in range(t):
    solve()