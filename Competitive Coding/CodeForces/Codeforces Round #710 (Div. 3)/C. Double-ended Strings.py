def solve(a, b, n, m):
    l = 0
    d = {ch:[] for ch in b}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            continue
    l = 0
    for i in range(m):
        if not d[b[i]]:
            continue
        for x in d[b[i]]:
            k = x
            res = 0
            for j in range(i, m):
                if k >= n:
                    l = max(l, res)
                    break
                if a[k] == b[j]:
                    res += 1
                else:
                    l = max(l, res)
                    res = 0
                k += 1
            else:
                l = max(l , res)
    return l

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    n = len(a)
    m = len(b)
    if m < n:
        l = solve(a, b, n, m)
    else:
        l = solve(b, a, m, n)
    ans = n+m - 2*l
    print(ans)
