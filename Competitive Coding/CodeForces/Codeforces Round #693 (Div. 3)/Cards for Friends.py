t = int(input())
for _ in range(t):
    w, h, n = [int(s) for s in input().split(" ")]
    c = 0
    while w%2 == 0:
        c += 1
        w = w//2
    while h%2 == 0:
        c += 1
        h = h//2
    ans = 2**c
    if ans >= n:
        print("YES")
    else:
        print("NO")
