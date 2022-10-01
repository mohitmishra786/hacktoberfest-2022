from math import *
from collections import Counter
from bisect import *
import sys
import fractions

def solve():
    x, y, a, b = [int(s) for s in input().split(" ")]
    # x is less than y
    if x > y:
        x, y = y, x
    # a is less than b
    if a > b:
        a, b = b, a
    if a == b:
        print(x//a)
        return
    xy_diff = y-x
    ab_diff = b-a
    take = xy_diff // ab_diff
    take = min([take, x//a, y//b])
    ans = take
    x -= take*a
    y -= take*b
    together = x//(a+b)
    ans += 2*together
    x -= together*(a+b)
    y -= together*(a+b)
    ans += min(x//a, y//b)
    print(ans)    

t = int(input())
for _ in range(t):
    solve()