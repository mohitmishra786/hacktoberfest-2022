t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    ans = [["." for i in range(m)] for j in range(n)]
    grid = []
    for i in range(n):
        row = input().strip()
        grid.append(row)

    for j in range(m):
        stoneCnt = 0
        for i in range(n):
            if grid[i][j] == "*":
                stoneCnt += 1
            elif grid[i][j] == "o":
                ans[i][j] = "o"
                curRow = i-1
                while stoneCnt:
                    ans[curRow][j] = "*"
                    curRow -= 1
                    stoneCnt -= 1

        if stoneCnt:
            curRow = n-1
            while stoneCnt:
                ans[curRow][j] = "*"
                curRow -= 1
                stoneCnt -= 1

    for i in range(n):
        print("".join(ans[i]))  
    
    