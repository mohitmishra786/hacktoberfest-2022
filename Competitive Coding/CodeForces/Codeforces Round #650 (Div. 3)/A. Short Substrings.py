t = int(input())
for _ in range(t):
    s = input()
    ans = s[0]
    for x in range(1, len(s)-1, 2):
        ans += s[x]
    ans += s[-1]
    print(ans)
