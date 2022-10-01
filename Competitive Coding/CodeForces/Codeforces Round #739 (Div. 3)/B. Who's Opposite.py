t = int(input())
for _ in range(t):
    a, b, c = [int(s) for s in input().split(" ")]
    diff = abs(a-b)
    tot = diff*2
    mx = max(a, b, c)
    if mx > tot:
        print(-1)
    elif diff + c <= tot:
        print(diff + c)
    elif c - diff >= 0:
        print(c - diff)
    else:
        print(-1)