from heapq import heapify, heappop

def getMx(mx, n, c):
    num = []
    vis = [0]*n
    lst = -1
    for i in range(n):
        if mx[i] == 0:
            for x in c:
                if x < lst and x not in num and not vis[x-1]:
                    num.append(-1*x)
            heapify(num)
            mx[i] = heappop(num)*(-1)
            vis[mx[i]-1] = 1
        else:
            lst = mx[i]
    return mx

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    d = [i for i in range(1, n+1) if i not in a]
    ans = [0]*n
    lst = -1
    for i in range(n):
        if lst < 0 or lst != a[i]:
            lst = a[i]
            ans[i] = a[i]
    if 0 not in ans:
        print(" ".join(map(str, ans)))
        print(" ".join(map(str, ans)))
    else:
        mn = ans.copy()
        mx = ans.copy()
        c = d.copy()
        heapify(d)
        for i in range(n):
            if mn[i] == 0:
                mn[i] = heappop(d)
        mx = getMx(mx, n, c)
        print(" ".join(map(str, mn)))
        print(" ".join(map(str, mx)))
        
