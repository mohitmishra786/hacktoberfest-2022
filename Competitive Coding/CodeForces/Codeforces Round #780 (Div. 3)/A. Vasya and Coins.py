t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    if not n:
        print(1)
        continue
    print(n+2*m + 1)