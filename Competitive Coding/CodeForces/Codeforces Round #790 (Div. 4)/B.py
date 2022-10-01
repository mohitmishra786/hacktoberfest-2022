t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    mn = min(a)
    ans = sum(a)-mn*n
    print(ans)