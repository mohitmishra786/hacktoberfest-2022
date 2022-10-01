def solve(l, r, arr, d, cur = 0):
    if l > r:
        return
    if l == r:
        d[l] = cur
    mx = l
    for i in range(l+1, r+1):
        if arr[mx] < arr[i]:
            mx = i
    d[mx] = cur
    solve(l, mx-1, arr, d, cur+1)
    solve(mx+1, r, arr, d, cur+1)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    d = [0]*n
    solve(0, n-1, arr, d)
    print(" ".join(map(str, d)))
        
