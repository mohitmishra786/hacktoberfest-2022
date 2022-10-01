def solve():
    s = input()
    if len(s) == 1:
        if s == "a":
            print("YES")
        else:
            print("NO")
        return
    a = {chr(i):None for i in range(97, 97+26)}
    for i in range(len(s)):
        if a[s[i]] is None:
            a[s[i]] = i
        else:
            print("NO")
            return
    lst = a["a"]
    l = 1
    r = 1
    cnt = len(s)-1
    for key, val in a.items():
        if not cnt:
            break
        if val is None:
            print("NO")
            return
        if key == 'a':
            continue
        cur = val - lst
        if cur < 0:
            if abs(cur) == l:
                l += 1
            else:
                print("NO")
                return
        else:
            if abs(cur) == r:
                r += 1
            else:
                print("NO")
                return
        cnt -= 1
    print("YES")

t = int(input())
for _ in range(t):
    solve()