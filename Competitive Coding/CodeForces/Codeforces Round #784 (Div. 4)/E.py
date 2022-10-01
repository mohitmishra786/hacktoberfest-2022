from collections import defaultdict, Counter

t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(int)
    s = []
    for i in range(n):
        let = input()
        s.append(let)

    count = Counter(s)
    ans = 0
    for ele, cnt in count.items():
        pass