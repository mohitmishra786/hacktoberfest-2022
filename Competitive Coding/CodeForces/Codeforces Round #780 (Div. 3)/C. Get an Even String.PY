t = int(input())
for _ in range(t):
    s = input()
    ans = 0
    d = {}
    for char in s:
        d[char] = d.get(char, 0) + 1
        ans += 1
        if d[char] == 2:
            ans -= 2
            d = {}
    print(ans)
    