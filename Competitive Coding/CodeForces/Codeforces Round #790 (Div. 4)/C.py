t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    words = []
    for i in range(n):
        s = input()
        words.append(s)

    ans = 1000000
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            cnt = 0
            for k in range(m):
                cnt += abs(ord(words[i][k]) - ord(words[j][k]))
            ans = min(ans, cnt)
    print(ans)