a = []
i = 1
while len(a) != 1000:
    if i%3 == 0:
        i += 1
        continue
    if str(i)[-1] == "3":
        i += 1
        continue
    a.append(i)
    i += 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(a[n-1])