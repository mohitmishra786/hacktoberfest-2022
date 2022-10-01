t = int(input())
for _ in range(t):
    n = int(input())
    count = n//2020
    rem = n%2020
    if rem <= count:
        print("YES")
    else:
        print("NO")
