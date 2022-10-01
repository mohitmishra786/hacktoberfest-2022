t = int(input())
for _ in range(t):
    n, m, x = [int(s) for s in input().split(" ")]
    c = x//n
    r = x%n
    if r:
        c += 1
        r -= 1
        ans = r*m + c
    else:
        ans = (n-1)*m + c
    print(ans)
