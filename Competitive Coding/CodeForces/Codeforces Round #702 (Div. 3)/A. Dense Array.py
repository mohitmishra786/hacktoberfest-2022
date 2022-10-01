def solve(a, b):
    res = 0
    mn = min(a, b)
    mx = max(a, b)
    while mn*2 < mx:
        res += 1
        mn *= 2
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    ans = 0
    for i in range(1, n):
        ans += solve(arr[i], arr[i-1])
    print(ans)
