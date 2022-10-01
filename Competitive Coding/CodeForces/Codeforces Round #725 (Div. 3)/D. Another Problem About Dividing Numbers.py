import math

def primeFactors(n):
    res = 0
    # Print the number of two's that divide n
    while n % 2 == 0:
        res += 1
        n = n // 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        # while i divides n , print i ad divide n
        while n % i== 0:
            res += 1
            n = n // i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        res += 1
    return res

def solve():
    a, b, k = [int(s) for s in input().split(" ")]
    g = math.gcd(a, b)
    fac_a = primeFactors(a)
    fac_b = primeFactors(b)
    if k == 1:
        if (a%b == 0 or b%a == 0) and a != b:
            print("YES")
        else:
            print("NO")
    else:
        if k <= fac_a + fac_b:
            print("YES")
        else:
            print("NO")

t = int(input())
for _ in range(t):
    solve()