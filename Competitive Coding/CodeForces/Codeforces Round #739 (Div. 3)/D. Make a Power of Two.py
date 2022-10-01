t = int(input())
for _ in range(t):
    s = input()
    ans = 64
    for i in range(60):
        powerOfTwo = str(1<<i)
        saved = 0
        k = 0
        while saved < len(powerOfTwo) and k < len(s):
            if powerOfTwo[saved] == s[k]:
                saved += 1
            k += 1
        ans = min(ans, len(s) + len(powerOfTwo) - 2*saved)
    print(ans)