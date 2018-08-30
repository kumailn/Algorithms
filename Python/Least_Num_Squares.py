# def leastNumSquares(num):
#     #Because of Lagrange's four square theorem, the max number can be 4
#     if(isSquare(num)):
#         return 1
#     # If num is not in the form of 4^k*(8*m + 7), due to Legendres theorem
#     while(n % 4 = 0):
        


def leastNumSquares(num):
    if(num <= 0):
        return 0
    elif(isSquare(num)):
        return 1
    l = [i for i in range(num + 1)]
    sqrs = [i**2 for i in range(1, int(num ** 0.5) + 1)]
    for i in l:
        for j in sqrs:
            if(i - j < 0):
                break
            l[i] = min(l[i], l[i - j] + 1)
    return l[-1]
    
    
def leastNumSquaresv2(num):
    if (num <= 0):
        return 0
    perfectSqCounts = [1]
    while len(perfectSqCounts) <= num:
        currentNum = len(perfectSqCounts)
        currentSquareCount = 4
        for i in range(1, currentNum + 1):
            print(i, currentNum)
            currentSquareCount = min(currentSquareCount, perfectSqCounts[currentNum - (i ** 2)] + 1)
        perfectSqCounts += [currentSquareCount]
    return perfectSqCounts[-1]

def isSquare(num):
    return (num ** 0.5) * (num ** 0.5) == num

print(leastNumSquaresv2(12))