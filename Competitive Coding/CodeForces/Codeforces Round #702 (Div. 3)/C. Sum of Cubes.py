import math

t = int(input())
for _ in range(t):
    x = int(input())
    a = math.floor(x**(1/3))
    b = 0
    flag = False
    while a >= b:
        if b == 0:
            if (a**3)*2 == x:
                flag = True
                break
        else:
            val = a**3 + b**3
            if val == x:
                flag = True
                break
            elif val > x:
                a -= 1
        b += 1
    if flag:
        print("YES")
    else:
        print("NO")
