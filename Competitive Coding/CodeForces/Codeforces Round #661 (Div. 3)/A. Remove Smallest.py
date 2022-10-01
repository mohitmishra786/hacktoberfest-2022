t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort()
    ans = "YES"
    for i in range(n-1):
        if a[i+1]-a[i] > 1:
            ans = "NO"
            break
    print(ans)
