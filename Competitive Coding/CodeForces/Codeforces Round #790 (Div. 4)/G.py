t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a = [-1] + a
    s = input()
    balance = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        if s[i] == "B":
            balance[i] += 1
        else:
            balance[i] -= 1
        
        if a[i] != -1:
            balance[a[i]-1] += balance[i]
    
    ans = 0
    for i in range(n):
        if balance[i] == 0:
            ans += 1
    print(ans)