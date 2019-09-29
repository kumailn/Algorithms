# Question: Find the index of the element in the list such that
#           the sum of elements to its left equals the sum of elements to its right
# Difficulty: Easy
# Solution: Store the sum of the left side and right side and adjust each loop and check
# Space Complexity: O(1)
# Time Complexity: O(n)

from typing import List

def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i, v in enumerate(nums):
            rightSum -= v     
            if leftSum == rightSum: return i
            leftSum += v
            
        return -1

