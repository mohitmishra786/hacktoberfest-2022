t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort()
    lst = a.pop()
    tot = sum(a)
    if tot > lst:
        diff = tot-lst
        if diff in a:
            a.remove(diff)
            print(" ".join(map(str, a)))
        else:
            lst = a.pop()
            tot -= lst
            if lst == tot:
                print(" ".join(map(str, a)))
            else:
                print(-1)
    else:
        lst = a.pop()
        tot -= lst
        if lst == tot:
            print(" ".join(map(str, a)))
        else:
            print(-1)
            
