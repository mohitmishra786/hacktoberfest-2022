t = int(input())
for _ in range(t):
    n = int(input())
    c1 = n//3
    c2 = n//3
    rem = n%3
    if rem!= 0:
        if rem&1:
            c1 += 1
        else:
            c2 += 1
    print(c1, c2)