def haha(s):
    return len([i for i in range(len(s) - 3) if s[i:i+4] == 'haha'])
 
 
def solve():
    vars = dict()
    for _ in range(int(input())):
        s = input().split()
        if s[1] == ':=':
            # store the first 3 and the last 3 for all the possiblities
            vars[s[0]] = (haha(s[2]), s[2][:3], s[2][-3:])
        else:
            a, b = vars[s[2]], vars[s[4]]
            vars[s[0]] = (a[0] + b[0] + haha(a[2] + b[1]), (a[1] + b[1])[:3], (a[2] + b[2])[-3:])
 
    print(vars[s[0]][0])
 
 
for _ in range(int(input())):
    solve()