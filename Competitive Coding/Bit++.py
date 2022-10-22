n=input()
n = n[1:-1]
split = n.split(", ")
lst=[]
for i in split:
    if i not in lst:
        if i != "":
            lst.append(i)
print(len(lst))
