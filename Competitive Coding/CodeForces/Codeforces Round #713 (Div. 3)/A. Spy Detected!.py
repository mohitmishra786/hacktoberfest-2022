t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    b = list(dict.fromkeys(a))
    for x in b:
        if a.count(x) == 1:
            print(a.index(x)+1)
            break
