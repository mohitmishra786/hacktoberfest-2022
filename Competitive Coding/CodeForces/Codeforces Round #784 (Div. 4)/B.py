from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
        if d[a[i]] == 3:
            print(a[i])
            break
    else:
        print("-1")