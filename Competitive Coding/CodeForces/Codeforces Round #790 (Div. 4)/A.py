def findSum(n):
    ans = 0
    while n > 0:
        ans += n%10
        n = n//10
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    first = findSum(n//1000)
    second = findSum(n%1000)
    if first == second:
        print("YES")
    else:
        print("NO")