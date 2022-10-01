t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        three = 0
        two = 0
        while n%3 == 0:
            three += 1
            n //= 3
        while n%2 == 0:
            two += 1
            n //= 2
        if n > 1:
            print(-1)
        elif three < two:
            print(-1)
        else:
            diff = three - two
            ans = three- diff + diff*2
            print(ans)
"""
0
-1
2
-1
-1
12
36
"""
