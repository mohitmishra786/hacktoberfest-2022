from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    vals = list(Counter(arr).values())
    vals.sort(reverse = True)
    ans = 0
    for i, b in enumerate(vals):
        ans = max(ans, b*(i+1))
    print(n-ans)
