def solve(arr, n, h, w):
    for i in range(n):
        if arr[i][0] < h and arr[i][1] < w:
            return i+1
        if arr[i][0] < w and arr[i][1] < h:
            return i+1
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[int(s) for s in input().split(" ")] for i in range(n)]
    ans = []
    for i in range(n):
        ans.append(solve(arr, n, arr[i][0], arr[i][1]))
    print(*ans)
