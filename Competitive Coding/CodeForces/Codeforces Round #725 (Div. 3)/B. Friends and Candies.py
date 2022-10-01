from typing import AnyStr


def solve():
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort()
    tot = sum(a)
    if tot%n != 0:
        print(-1)
        return
    av = tot//n
    ans = 0
    for x in a:
        if x > av:
            ans += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()