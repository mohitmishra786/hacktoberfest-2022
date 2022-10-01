def solve():
    n, k = [int(s) for s in input().split(" ")]
    if k == 1:
        if len(set(str(n))) == 1:
            print(n)
        else:
            s = str(n)
            first  = s[0]
            l = len(s)
            if int(first*l) >= n:
                print(first*l)
            else:
                if first != 9:
                    print(int(str(int(first)+1)*l))
                else:
                    print("1"*(l+1))
    else:
        num = sorted(list(map(int, str(n))))
        s = str(n)
        first = s[0]
        l = len(s)

    return

t = int(input())
for _ in range(t):
    solve()