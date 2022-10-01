t = int(input())
for _ in range(t):
    x, y, k = [int(s) for s in input().split(" ")]
    cur = k%x
    if cur == y:
        print(k)
    elif cur > y:
        print(k-cur+y)
    else:
        print(k-x+y-cur)

