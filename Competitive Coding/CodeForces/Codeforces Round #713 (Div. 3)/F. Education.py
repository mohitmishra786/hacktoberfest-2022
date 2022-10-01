t = int(input())
for _ in range(t):
    n, c = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    b = [int(s) for s in input().split(" ")]
    ans = (c+a[0]-1)//a[0]
    i = 1
    tot = 1
    left = 0
    while i < n:
        x = ((b[i-1]+a[i-1]-left-1)//a[i-1]) + 1
        tot += x
        left += x*a[i-1] - b[i-1]
        cur = ((c-left+a[i]-1)//a[i])+tot
        ans = min(ans, cur)
        i += 1
    print(ans)
        
