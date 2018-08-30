'''Given a decoding for each letter in the alphaber (A-> 1, ... Z-> 26) determine
the number of ways a given string of digits could be interpereted'''

# Generic recursive solution
def numDecodings(s, l):
    startIndex = len(s) - l
    if(l == 0):
        return 1
    if(s[startIndex] == '0'):
        "ONEE"
        return 0
    res = numDecodings(s, l - 1)
    if(l >= 2 and int(s[startIndex] + s[startIndex + 1]) <= 26):
        res += numDecodings(s, l - 2)
    return res
                
data = '110'
print(numDecodings('110', len('110')))