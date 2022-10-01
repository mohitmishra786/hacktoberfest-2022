from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    d = Counter(a)
    count = list(d.values())
    count.sort()
    l = len(count)
    lst = count.pop()
    if sum(count) < lst:
        ans = n - 2*sum(count)
    else:
        ans = n%2
    print(ans)
        
