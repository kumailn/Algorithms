def longest(substr):
    i, j = 0, -1
    maxlen = 0
    for k in range(1, len(substr)):
        if substr[k] == substr[k-1]: continue
        if j > -1 and substr[k] != substr[j]:
            maxlen = max(maxlen, k - i)
            i = j