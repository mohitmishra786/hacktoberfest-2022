t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    ans = 0
    b = [0]*n
    for i in range(n-1, -1, -1):
        b[i] = arr[i]
        if i + arr[i] < n:
            b[i] += b[i+ arr[i]]
        ans = max(ans, b[i])
    print(ans)
