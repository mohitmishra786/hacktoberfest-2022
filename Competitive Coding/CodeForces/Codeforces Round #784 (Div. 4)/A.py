t = int(input())
for _ in range(t):
    n = int(input())
    if n >= 1900:
        print("Division 1")
    elif n >=1600:
        print("Division 2")
    elif n >= 1400:
        print("Division 3")
    else:
        print("Division 4")
