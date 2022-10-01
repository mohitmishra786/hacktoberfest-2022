t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split(" ")]
    memo = [int(s) for s in input().split(" ")]
    con = [int(s) for s in input().split(" ")]
    tot = sum(memo)
    if tot < m:
        print(-1)
    elif tot == m:
        print(sum(con))
    else:
        reg = []
        imp = []
        ans = 0
        for i in range(n):
            if con[i] == 1:
                reg.append(memo[i])
            else:
                imp.append(memo[i])
        reg.sort()
        imp.sort()
        cur = sum(reg)
        if cur == m:
            print(len(reg))
        elif cur > m:
            while reg:
                m -= reg.pop()
                ans += 1
                if m <= 0:
                    break
            print(ans)
        else:
            # Deleting all the regular apps and deleting the imp
            res = len(reg)
            curMemo = m
            curMemo -= cur
            i = 1
            while curMemo > 0:
                curMemo -= imp[-i]
                res += 2
                i += 1
            # Deleting all the imp apps
            if sum(imp) == m:
                res1 = len(imp)*2
            # Deleting some imp apps
            elif sum(imp) > m:
                cur = m
                i = 1
                res1 = 0
                while cur > 0:
                    cur -= imp[-i]
                    i += 1
                    res1 += 2
            # Deleting the imp apps first and deleting then reg
            else:
                res1 = len(imp)*2
                mem = m - sum(imp)
                j = 1
                while mem > 0:
                    res1 += 1
                    mem -= reg[-j]
                    j += 1
            # Deleting from both the lists
            imp_p = 1
            reg_p = 1
            curMem = m
            res2 = 0
            while curMem > 0:
                if reg[-reg_p] > imp[-imp_p]:
                    cur_Mem -= reg[-reg_p]
                    reg_p += 1
                    res2 += 1
                else:
                    curMem -= imp[-imp_p]
                    imp_p += 1
                    res2 += 2
            mn = min(res, res1)
            mn = min(mn, res2)
            print(mn)
                

            
    
