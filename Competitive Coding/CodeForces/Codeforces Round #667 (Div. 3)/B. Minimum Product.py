def solve(a, b, x, y, n):
    diff = a - x
    if diff >= n:
        a -= n
        return a*b
    else:
        a -= diff
        n -= diff
    diff2 = b-y
    if diff2 >= n:
        b -= n
    else:
        b -= diff2
    return a*b
        

t = int(input())
for _ in range(t):
    a, b, x, y, n = [int(s) for s in input().split(" ")]
    tempa, tempb = a, b
    ans1 = solve(tempa, tempb, x, y, n)
    ans2 = solve(b, a, y, x, n)
    print(min(ans1, ans2))
