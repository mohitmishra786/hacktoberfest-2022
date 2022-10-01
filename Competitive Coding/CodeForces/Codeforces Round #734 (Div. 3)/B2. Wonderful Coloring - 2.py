def solve():
    n, k = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    d = dict()
    ans = []
    times = [k]*k
    for x in a:
        val = d.get(x, None)
        if not val:
            d[x] = 1
            ans.append(1)
        else:
            if val == k:
                ans.append(0)
            else:
                d[x] += 1
                ans.append(d[x])
    print(*ans)

t = int(input())
for _ in range(t):
    solve()