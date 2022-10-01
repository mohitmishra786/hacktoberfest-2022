def binarySearch(arr, n):
    mn = arr[0]
    sm = arr[0]
    for i in range(1, n):
        if arr[i] > sm:
            mn = arr[i]
        sm += arr[i]
    return mn

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    acs = sorted(arr)
    low = binarySearch(acs,n)
    ans = []
    for i in range(n):
        if arr[i] >= low:
            ans.append(i+1)
    print(len(ans))
    print(" ".join(map(str, ans)))
