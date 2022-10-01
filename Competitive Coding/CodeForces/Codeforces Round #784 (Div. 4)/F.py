t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    ans = 0
    
    sumL = a[0]
    sumR = a[n-1]

    l = 0
    r = n-1

    while l < r:
        if sumL == sumR:
            ans = max(ans, l+1+n-r)
        if sumL <= sumR:
            l += 1
            sumL += a[l]
        if sumR < sumL:
            r -= 1
            sumR += a[r]
    print(ans)