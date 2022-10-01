t = int(input())
for _ in range(t):
    n,k = [int(s) for s in input().split(" ")]
    arr = input()
    ans = 0
    if "1" not in arr:
        ans = n//k
    else:
        zeros = arr.split("1")
        zeros = [ch for ch in zeros if ch !=""]
        print(zeros)
        for i in range(len(zeros)):
            if i == 0 and arr[0] != "1":
                a = (len(zeros[i])-k)//n
                if a > 0:
                    ans += a
            elif i == len(zeros)-1 and arr[-1] != "1":
                a = (len(zeros[i])-k)//n
                if a > 0:
                    ans += a
            else:
                a = (len(zeros[i])-2*k)//n
                if a > 0:
                    ans += a
    print(ans)
