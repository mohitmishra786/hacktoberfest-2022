t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    one = 0
    two = 0
    for x in arr:
        if x == 1:
            one += 1
        else:
            two += 1
    if one != 0 and one%2 == 0:
        print("YES")
    elif one == 0 and two%2 == 0:
        print("YES")
    else:
        print("NO")
