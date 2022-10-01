t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(s) for s in input().split(" ")]
    arr.sort()
    alice = 0
    bob = 0
    for i in range(1, n+1):
        if i%2 == 1:
            if arr[-i]%2 == 0:
                alice += arr[-i]
            else:
                continue
        else:
            if arr[-i]%2 == 1:
                bob += arr[-i]
            else:
                continue
    if bob == alice:
        print("Tie")
    elif bob > alice:
        print("Bob")
    else:
        print("Alice")
