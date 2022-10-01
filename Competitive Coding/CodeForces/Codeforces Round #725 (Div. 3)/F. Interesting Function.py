import sys

def find(n):
    res = n
    cur = 1
    times = sys.maxsize
    while times > 0:
        times = n//(10**cur)
        res += times
        cur += 1
    return res

def solve():
    l, r = [int(s) for s in input().split(" ")]
    ans = find(r) - find(l)
    print(ans)

t = int(input())
for _ in range(t):
    solve()