t = int(input())
for _ in range(t):
    n = int(input())
    if bin(n).count("1") == 1:
        print("NO")
    else:
        print("YES")
