def solve(nums, x, d, n):
    if sum(nums) < 0:
        return -1
    cnt = 0
    sm = 0
    flag = 0
    while True:
        for i in range(n):
            sm += nums[i]
            if sm == x:
                return cnt
            d[sm] = cnt
            cnt += 1
            if x < sm:
                flag += 1
        if flag == n-1:
            return -1
    

t = int(input())
for _ in range(t):
    n,m = [int(s) for s in input().split(" ")]
    nums = [int(s) for s in input().split(" ")]
    ques = [int(s) for s in input().split(" ")]
    ans = []
    d = {}
    for x in ques:
        if x in d:
            ans.append(d[x])
        else:
            ans.append(solve(nums, x, d, n))
    print(" ".join(map(str, ans)))
