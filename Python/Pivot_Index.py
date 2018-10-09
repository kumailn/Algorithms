#The pivot index is the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
#If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

#Naive brute force solution, re-calculate left and right side each iteration.
def pivot(nums):
  total = sum(nums)
  for i in range(len(nums)):
    left_sum = sum(nums[:i])
    if(left_sum == total-left_sum-nums[i]):
      return i
  return -1

#Optimal solution, keep value of left and right sides and ajust accordingly 
def pivot2(nums):
        if not nums: return -1
        leftSum, rightSum = 0, sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            if(leftSum == rightSum): return i
            leftSum += nums[i]
        return -1
            
            
print(pivot([1, 7, 3, 6, 5, 6]))
print(pivot2([1, 7, 3, 6, 5, 6]))