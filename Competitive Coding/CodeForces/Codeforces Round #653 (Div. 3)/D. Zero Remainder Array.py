from collections import Counter

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    arr = [int(s)%k for s in input().split(" ")]
    arr.sort()
    count = Counter(arr)
    x = 0
    for key, val in count.items():
        if key == 0:
            continue
        x = max(x, (k-key)+ k*(val-1))
    if x:
        print(x+1)
    else:
        print(x)


"""
6
18
0
227
8
"""
