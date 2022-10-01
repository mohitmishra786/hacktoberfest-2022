from collections import deque
 
for _ in range(int(input())):
    n = int(input())
    q = list(map(int, input().split()))
    pmn, pmx = deque(), []
    mn, mx = [], []
    cur = 1
    i = 0
    while i < n:
        mn.append(q[i])
        mx.append(q[i])
        while cur < q[i]:
            pmn.append(cur)
            pmx.append(cur)
            cur += 1
        cur += 1
        j = i + 1
        while j < n and q[i] == q[j]:
            j += 1
        for _ in range(j - i - 1):
            mn.append(pmn.popleft())
            mx.append(pmx.pop())
        i = j
    print(*mn)
    print(*mx)
