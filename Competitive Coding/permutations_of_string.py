def permute(data, i):
    n = len(data)

    if i == n:
        print(''.join(data))
    else:
        for j in range(i, n):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1)
            data[i], data[j] = data[j], data[i]


test_string = "abc"
data = list(test_string)
permute(data, 0)
