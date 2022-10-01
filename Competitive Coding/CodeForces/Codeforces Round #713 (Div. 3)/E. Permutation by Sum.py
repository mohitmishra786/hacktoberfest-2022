def out(ans, n):
    num = [i for i in range(1, n+1) if i not in ans]
    for i in range(n):
        if ans[i] == 0:
            ans[i] = num.pop()
    print(" ".join(map(str, ans)))

t = int(input())
for _ in range(t):
    n, l, r, s = [int(x) for x in input().split(" ")]
    ans = [0]*n
    ex = r-l+1
    low = (ex*(ex+1))//2
    high = 0
    lst = n
    for i in range(ex):
        high += lst
        lst -= 1
    if s < low or s > high:
        print(-1)
        continue
    lst = 1
    tot = 0
    for i in range(l-1, r):
        ans[i] = lst
        lst += 1
        tot += ans[i]
    pos = r-1
    nxt = n
    while tot != s:
        if ans[pos] == nxt:
            nxt -= 1
            pos -= 1
        ans[pos] += 1
        tot += 1
    out(ans, n)
        
