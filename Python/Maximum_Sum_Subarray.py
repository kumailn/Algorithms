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

#More compact solution        
def maxSubArray(self, nums):
        cmax = gmax = nums[0] if nums else 0
        for i, v in enumerate(nums[1:]):
            cmax = max(cmax + v, v)
            if cmax > gmax: gmax = cmax
        return gmax

print(maxsumsub([-2,1,-3,4,-1,2,1,-5,4]))