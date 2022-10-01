from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    words = defaultdict(int)
    orderOfWords = []

    for i in range(n):
        word = input()
        words[word] = 1
        orderOfWords.append(word)
    
    ans = ["0"]*n
    for idx, word in enumerate(orderOfWords):
        l = len(word)
        for i in range(1, l):
            curword = word[:i]
            if words[curword] == 1 and words[word[i:]] == 1:
                ans[idx] = "1"
    print("".join(ans))