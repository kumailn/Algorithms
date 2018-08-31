'''Given a decoding for each letter in the alphaber (A-> 1, ... Z-> 26) determine
the number of ways a given string of digits could be interpereted'''

# Generic recursive solution
def numDecodings(inputDigits, l):
    startIndex = len(inputDigits) - l
    if(l == 0):
        return 1
    if(inputDigits[startIndex] == '0'):
        "ONEE"
        return 0
    res = numDecodings(inputDigits, l - 1)
    if(l >= 2 and int(inputDigits[startIndex] + inputDigits[startIndex + 1]) <= 26):
        res += numDecodings(inputDigits, l - 2)
    return res

# Recursive solution with memoization
def numDecodingsDP(s, l, store):
    startIndex = len(s) - l
    if(l == 0):
        return 1
    if(s[startIndex] == '0'):
        return 0
    if(store[l] != None):
        return store[l]
    res = numDecodingsDP(s, l - 1, store)
    if(l >= 2 and int(s[startIndex] + s[startIndex + 1]) <= 26):
        res += numDecodingsDP(s, l - 2, store)
    store[l] = res
    return res  

data = '11111111111111111111'
print(numDecodings(data, len(data)))
print(numDecodingsDP(data, len(data), [None for i in range(len(data) + 1)]))


