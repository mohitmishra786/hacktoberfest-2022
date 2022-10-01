t = int(input())
for _ in range(t):
    n, k = [int(s) for s in input().split(" ")]
    s = input()
    s = list(s)
    ans = 0
    for i in range(len(s)):
        if s[i] == "*":
            s[i] = "x"
            ans += 1
            break
    for i in range(len(s)-1, 0, -1):
        if s[i] == "*":
            s[i] = "x"
            ans += 1
            break
    index =[]
    for i in range(len(s)):
        if s[i] == "*":
            index.append(i)
        elif s[i] == "x":
            index.append(i)
    st = index[0]
    lst = st
    for i in range(1, len(index)):
        if index[i]-st <= k:
            lst = index[i]
        else:
            ans += 1
            st = lst
            lst = index[i]
    print(ans)
        
