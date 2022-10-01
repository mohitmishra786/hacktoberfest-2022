from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    d = defaultdict(int)
    ans = 0
    for char in s:
        if d[char] == 0:
            ans += 2
        else:
            ans += 1
        d[char] += 1
    print(ans)