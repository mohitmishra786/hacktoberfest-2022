t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    odd = 0
    even = 0
    for i in range(n):
        if i%2 != arr[i]%2:
            if i%2 == 0:
                even += 1
            else:
                odd += 1
        else:
            continue
    if odd == even:
        print(odd)
    else:
        print(-1)
