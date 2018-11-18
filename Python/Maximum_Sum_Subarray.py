#Question: Find the sum of a continious subarray in an array with the largest sum
#Solution: Kadanes algorithm
#Difficulty: Easy

#Optimal solution using Kadanes algorithm
def maxsumsub(arr):
    #If list is empty the sum is 0
    if not arr: return 0
    #Store the current maximum and global maximum, set both to sub array consisting of first element initially
    currentMax = globalMax = arr[0]
    #Loop from 1 to end (Since current and global max already have 0th element)
    for i in range(1, len(arr)):
        #Set current max to be the max of just the current element, or the current element + the current max calculated
        currentMax = max(arr[i], currentMax + arr[i])
        #If current max turns out to be larger than global, make global current
        if(globalMax < currentMax): globalMax = currentMax
    return globalMax

#More compact solution        
def maxSubArray(self, nums):
        cmax = gmax = nums[0] if nums else 0
        for i, v in enumerate(nums[1:]):
            cmax = max(cmax + v, v)
            if cmax > gmax: gmax = cmax
        return gmax

print(maxsumsub([-2,1,-3,4,-1,2,1,-5,4]))