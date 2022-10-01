t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    first = a[0]%2
    second = a[1]%2
    ans = "YES"
    for i in range(n):
        if i % 2 == 0 and a[i] % 2 == first:
            continue
        if i % 2 == 1 and a[i] % 2 == second:
            continue
        ans = "NO"
        break
    print(ans)
