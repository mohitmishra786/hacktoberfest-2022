t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    b = [int(s) for s in input().split(" ")]
    mn_a = min(a)
    mn_b = min(b)
    ans = 0
    for i in range(n):
        req_a = a[i]-mn_a
        req_b = b[i]-mn_b
        ans += min(req_a, req_b) + abs(req_a-req_b)
    print(ans)
