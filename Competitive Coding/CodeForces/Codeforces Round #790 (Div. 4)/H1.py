t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] >= a[j]:
                ans += 1
    print(ans)