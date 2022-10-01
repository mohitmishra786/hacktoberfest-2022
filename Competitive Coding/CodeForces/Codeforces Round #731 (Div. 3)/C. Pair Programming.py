def solve():
    line = input()
    k, n, m = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    b = [int(s) for s in input().split(" ")]
    ans = []
    pointera = 0
    pointerb = 0
    while pointera != n or pointerb != m:
        if pointera != n and a[pointera] == 0:
            ans.append(0)
            k += 1
            pointera += 1
        elif pointerb != m and b[pointerb] == 0:
            ans.append(0)
            k += 1
            pointerb += 1
        elif pointera != n and a[pointera] <= k:
            ans.append(a[pointera])
            pointera += 1
        elif pointerb != m and b[pointerb] <= k:
            ans.append(b[pointerb])
            pointerb += 1
        else:
            print(-1)
            return
    print(*ans)
    

t = int(input())
for _ in range(t):
    solve()