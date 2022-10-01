def binarySearch(val, n, arr):
    if val > arr[-1]:
        return -1
    l = -1
    r = n
    while r > l+1:
        mid = (l+r)//2
        if arr[mid] < val:
            l = mid
        else:
            r = mid
    return r

t = int(input())
for _ in range(t):
    n, q = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]
    a.sort(reverse=True)

    for i in range(1, n):
        a[i] += a[i-1]
    
    for j in range(q):
        num = int(input())
        ans = binarySearch(num, n, a)
        if ans != -1:
            print(ans + 1)
        else:
            print(ans)    
