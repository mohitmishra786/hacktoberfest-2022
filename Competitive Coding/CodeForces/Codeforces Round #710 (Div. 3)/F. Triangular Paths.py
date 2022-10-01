def calc_dist(r1, c1, r2, c2):
    if r1-c1 == r2-c2:
        if (r1+c1)%2 == 1:
            return 0
        else:
            return r2-r1
    r2 -= r1 - 1
    c2 -= c1 - 1
    if (r1+c1)%2 == 0:
        return (r2-c2)//2
    else:
        return (r2-c2+1)//2

t = int(input())
for _ in range(t):
    n = int(input())
    r = [int(s) for s in input().split(" ")]
    c = [int(s) for s in input().split(" ")]
    pts = list(zip(r, c))
    pts.sort()
    cur_r = 1
    cur_c = 1
    ans = 0
    for nxt_r, nxt_c in pts:
        ans += calc_dist(cur_r, cur_c, nxt_r, nxt_c)
        cur_r = nxt_r
        cur_c = nxt_c
    print(ans)
    
