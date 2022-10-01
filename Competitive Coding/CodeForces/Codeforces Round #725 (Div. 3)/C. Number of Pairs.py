def solve():
    n, l, r = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            val = a[i] + a[j]
            if val >= l and val <= r:
                ans += 1
            else:
                continue
    print(ans)

t = int(input())
for _ in range(t):
    solve()