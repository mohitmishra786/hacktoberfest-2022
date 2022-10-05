#github - akrishna5

m, n = map(int, input().split(' '))

lst = list(map(int, input().split(' ')))

newlst = lst[n-1]

count = 0

for i in lst:

    if i >= newlst and (i > 0 and newlst > 0):
        count = count + 1

print(count)
