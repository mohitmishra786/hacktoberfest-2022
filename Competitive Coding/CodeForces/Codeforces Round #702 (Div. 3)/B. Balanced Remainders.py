t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    rem = [i%3 for i in arr]
    c0 = rem.count(0)
    c1 = rem.count(1)
    c2 = rem.count(2)
    req = n//3
    c0 -= req
    c1 -= req
    c2 -= req
    ans = 0
    while not(c1 == c2 and c2 == c0) or c1 != 0:
        if c0 > 0:
            c1 += c0
            ans += c0
            c0 = 0
        if c1 > 0:
            c2 += c1
            ans += c1
            c1 = 0
        if c2 > 0:
            c0 += c2
            ans += c2
            c2 = 0
    print(ans)
