#Optimal solution using Kadanes algorithm
def maxsumsub(arr):
    if(len(arr) == 0):
        return 0
    currentMax = globalMax = arr[0]
    for i in range(1, len(arr)):
        currentMax = max(arr[i], currentMax + arr[i])
        if(globalMax < currentMax):
            globalMax = currentMax
    return globalMax
        
print(maxsumsub([-2,1,-3,4,-1,2,1,-5,4]))