from collections import Counter

def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (n-1)*n//2

t = int(input())
for _ in range(t):
    a, b, k = [int(s) for s in input().split(" ")]
    boys = [int(s) for s in input().split(" ")]
    girls = [int(s) for s in input().split(" ")]
    boy = Counter(boys).values()
    girl = Counter(girls).values()
    ans = solve(k)
    for x in boy:
        if x >= 2:
            ans -= solve(x)
    for y in girl:
        if y >= 2:
            ans -= solve(y)
    print(ans)
    
