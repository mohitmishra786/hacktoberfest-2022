t = int(input())
for _ in range(t):
    a, b = [int(s) for s in input().split(" ")]
    s = input()
    l = a+b
    a -= s.count("0")
    b -= s.count("1")
    s = list(s)
    ans = None
    for i in range(l//2):
        if s[i] == s[l-i-1]:
            if s[i] == "?":
                s[i] = "*"
        elif s[i] == "1":
            if s[l-i-1] == "0":
                ans = -1
                break
            else:
                s[l-i-1] = "1"
                b -= 1
        elif s[i] == "0":
            if s[l-i-1] == "1":
                ans = -1
                break
            else:
                s[l-i-1] = "0"
                a -= 1
        else:
            s[i] = s[l-i-1]
            if s[i] == "1":
                b -= 1
            else:
                a -= 1

    for i in range(l//2):
        if s[i] == "*":
            if a >= 2:
                s[i] = "0"
                s[l-i-1] = "0"
                a -= 2
            else:
                s[i] = "1"
                s[l-i-1] = "1"
                b -= 2
    if s[l//2] == "?":
        if a:
            s[l//2] = "0"
            a -= 1
        else:
            s[l//2] = "1"
            b -= 1
    if a==0 and b ==0 and ans != -1:
        print("".join(s))
    else:
        print(-1)
