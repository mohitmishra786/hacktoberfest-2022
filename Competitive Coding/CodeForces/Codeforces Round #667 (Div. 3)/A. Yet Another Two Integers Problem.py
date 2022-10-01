t = int(input())
for _ in range(t):
    a, b = [int(s) for s in input().split(" ")]
    ans = (abs(a-b)+9)//10
    print(ans)
            
