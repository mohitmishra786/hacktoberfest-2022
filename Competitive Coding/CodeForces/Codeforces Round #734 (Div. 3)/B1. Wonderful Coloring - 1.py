def solve():
    s = input()
    ans = 0
    odd = 0
    d = {chr(i):0 for i in range(97, 97+26)}
    for ch in s:
        d[ch] += 1
    for char, occ in d.items():
        if occ == 0:
            continue
        if occ == 1:
            odd += 1
        else:
            ans += 1
    ans += odd//2
    print(ans)

t = int(input())
for _ in range(t):
    solve()