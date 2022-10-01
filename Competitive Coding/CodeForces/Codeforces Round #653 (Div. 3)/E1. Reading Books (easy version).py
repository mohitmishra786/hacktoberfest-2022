n, k = [int(s) for s in input().split(" ")]
alice = []
bob = []
both = []
for i in range(n):
    t, a, b = list(map(int, input().split(" ")))
    if a == b == 1:
        both.append(t)
    elif a == 1:
        alice.append(t)
    elif b == 1:
        bob.append(t)
    else:
        continue

alice.sort()
bob.sort()

for i in range(min(len(alice), len(bob))):
    both.append(alice[i] + bob[i])

both.sort()

if k > len(both):
    print(-1)
else:
    print(sum(both[:k]))
