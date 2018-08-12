#The pivot index is the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
#If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

def pivot(nums):
  total = sum(nums)
  for i in range(len(nums)):
    left_sum = sum(nums[:i])
    print(left_sum)
    if(left_sum == total-left_sum-nums[i]):
      return i
  return -1

print(pivot([1, 7, 3, 6, 5, 6]))