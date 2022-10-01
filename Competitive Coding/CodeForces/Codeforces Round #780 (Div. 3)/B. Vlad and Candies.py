t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    if n == 1:
        if a[0] == 1:
            print("YES")
        else:
            print("NO")
        continue
    a.sort()
    if a[n-1] - a[n-2] <= 1:
        print("YES")
    else:
        print("NO")