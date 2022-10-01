t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    br = []
    ans = 0
    for i in range(n):
        if s[i] == "(":
            br.append("(")
        else:
            if not br:
                ans += 1
            else:
                br.pop()
    print(ans)
