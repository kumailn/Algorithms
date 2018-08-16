def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    total = 1
    if(len(s) == 1 and s[0] == '0'):
        return 0
    for i in range(len(s) - 1):
        if(i == 0 and int(s[i]) == 0):
            return 0
        if(int(s[i + 1]) == 0):
            total -= 1
        if(int(s[i]) == 1 and int(s[i+1]) <= 9):
            total += 1
        elif(int(s[i]) == 2 and int(s[i+1]) <= 6):
            total += 1
    if total < 0:
        return 0
    return total
                
                
                
print(numDecodings('110'))