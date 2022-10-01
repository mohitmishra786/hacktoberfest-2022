def isValid(b, r):
    if b == 0 and r == 0:
        return True
    if b == 0 or r == 0:
        return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    b = 0
    r = 0
    for i in range(n):
        if s[i] == "B":
            b += 1
        elif s[i] == "R":
            r += 1
        else:
            if isValid(b, r):
                b = 0
                r = 0
            else:
                print("NO")
                break
    else:
        if isValid(b, r):
            print("YES")
        else:
            print("NO")