def maxprod(arr):
    currentMax = globalMax = arr[0]
    for i in range(1, len(arr)):
        currentMax = max(arr[i], arr[i] * currentMax)
        if(currentMax > globalMax):
            print(arr[i], currentMax, globalMax)
            globalMax = currentMax
    return globalMax

print(maxprod([2,3,-2,4]))