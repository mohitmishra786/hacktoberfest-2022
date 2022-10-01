def solve():
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    mx = a.index(1)
    mn = a.index(n)
    if mn > mx:
        mn, mx = mx, mn
    ans = mx+1
    ans = min(ans, n-mn)
    front = mn+1 + n-mx
    ans = min(ans, front)
    print(ans)

t = int(input())
for _ in range(t):
    solve()