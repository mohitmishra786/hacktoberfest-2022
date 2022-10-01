from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    c = Counter(a)
    r = [0]*101
    for x in c:
        for y in c:
            r[x+y] += min(c[x], c[y])
    print(max(r)//2)
