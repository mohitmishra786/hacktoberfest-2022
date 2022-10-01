t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        a.append(list(s))
    pts = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == "*":
                pts.append((i, j))
    x1, y1 = pts.pop()
    x2, y2 = pts.pop()
    if x1 == x2:
        if x1 > 0:
            a[x1-1][y1] = "*"
            a[x2-1][y2] = "*"
        else:
            a[x1+1][y1] = "*"
            a[x2+1][y2] = "*"
    elif y1 == y2:
        if y1 > 0:
            a[x1][y1-1] = "*"
            a[x2][y2-1] = "*"
        else:
            a[x1][y1+1] = "*"
            a[x2][y2+1] = "*"
    else:
        a[x1][y2] = "*"
        a[x2][y1] = "*"
    for i in range(n):
        print("".join(a[i]))
