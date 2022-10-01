from collections import defaultdict


t = int(input())
for _ in range(t):
    n, k = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    cnt = defaultdict(int)
    for ele in a:
        cnt[ele] += 1

    a = []
    for key, val in cnt.items():
        if val >= k:
            a.append(key)
    a.sort()

    if not a:
        print(-1)
        continue

    last = a[0]
    count = 0
    l, r = a[0], a[0]

    for i in range(1, len(a)):
        if a[i] == a[i-1] + 1:
            if a[i] - last > count:
                r = a[i]
                l = last
                count = a[i] - last
        else:
            last = a[i]
    print(l, r)

    

