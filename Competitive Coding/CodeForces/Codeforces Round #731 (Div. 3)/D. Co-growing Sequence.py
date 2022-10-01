def solve():
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    res = 0
    ans = []
    for i in range(n):
        res |= a[i]
        ans.append(res^a[i])
    print(*ans)

t = int(input())
for _ in range(t):
    solve()