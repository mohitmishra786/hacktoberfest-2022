t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        row = [int(s) for s in list(input())]
        grid.append(row)
    
    ans = 0
    
    for row in range(n):
        for col in range(n//2):
            if grid[row][col] != grid[row][n-col-1]:
                grid[row][col] = 1
                grid[row][n-col-1] = 1
                ans += 1
    
    new = []
    for col in range(n):
        cur = []
        for row in range(n):
            cur.append(grid[row][col])
        new.append(cur)
    
    for row in range(n):
        for col in range(n):
            if grid[row][col] != new[row][col]:
                grid[row][col] = 1
                new[row][col] = 1
                ans += 1
    print(ans)
