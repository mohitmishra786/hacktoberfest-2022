import math

def solve():
    k = int(input())
    sq = math.sqrt(k)
    low = math.floor(sq)
    high = math.ceil(sq)
    low = low*low
    high = high*high
    if low == high:
        print(int(sq), 1)
        return
    dis = k - low
    diff = (high - low + 1)//2
    r, c = 0, 0
    if dis <= diff:
        c = int(math.sqrt(high))
        r = dis
    else:
        r = int(math.sqrt(high))
        dis -= r
        c = r - dis
    print(r, c)

t = int(input())
for _ in range(t):
    solve()