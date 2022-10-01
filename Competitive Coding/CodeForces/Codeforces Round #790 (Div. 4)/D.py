t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    original = [[int(s) for s in input().split(" ")] for i in range(n)]
    matrix = [[0 for i in range(m)] for j in range(n)]

    # Right Diag
    orgJ = 0
    while orgJ < m:
        i = 0
        j = orgJ
        curI = i
        curJ = j
        val = 0
        while i < n and j < m:
            val += original[i][j]
            i += 1
            j += 1
        while curI < n and curJ < m:
            matrix[curI][curJ] = val
            curJ += 1
            curI += 1
        orgJ += 1
    
    orgI = n-1
    while orgI > 0:
        i = orgI
        j = 0
        curI = i
        curJ = j
        val = 0
        while i < n and j < m:
            val += original[i][j]
            i += 1
            j += 1
        while curI < n and curJ < m:
            matrix[curI][curJ] = val
            curI += 1
            curJ += 1
        orgI -= 1
    
    orgI = 0
    while orgI < n:
        i = orgI 
        j = 0 
        curI = i
        curJ = j
        val = 0
        while i < n and j < m and i >= 0 and j >= 0:
            val += original[i][j]
            i -= 1
            j += 1
        while curI< n and curJ < m and curI >= 0 and curJ >= 0:
            matrix[curI][curJ] += val - original[curI][curJ]
            curI -= 1
            curJ += 1
        orgI += 1
    
    orgJ = 1
    while orgJ < m:
        i = n-1
        j = orgJ
        curI = i
        curJ = j
        val = 0
        while i < n and j < m and i >= 0 and j >= 0:
            val += original[i][j]
            i -= 1
            j += 1
        while curI< n and curJ < m and curI >= 0:
            matrix[curI][curJ] += val - original[curI][curJ]
            curI -= 1
            curJ += 1
        orgJ += 1
    
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, matrix[i][j])
    print(ans)

    

