from collections import Counter, OrderedDict
from math import factorial

mod = 10**9 + 7
t = int(input())
for _ in range(t):
    n, k = [int(s) for s in input().split(" ")]
    arr = [int(s) for s in input().split(" ")]
    count = Counter(arr)
    counts = list(count.items())
    counts.sort(key=lambda x: x[0])
    ans = 1
    while k:
        key, val = counts.pop()
        if val <= k:
            k -= val
        else:
            ans *= factorial(val)//(factorial(val-k)*factorial(k))
            k = 0
    print(ans%mod)
