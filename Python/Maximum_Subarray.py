# Question: Find the sum of a continuous subarray in an array with the largest sum
# Solution: Kadane's algorithm (explained below)
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)
   
from typing import List

def maxSubArray(nums: List[int]) -> int:
        # Initialize a store for the local and global maximum sumarrays
        localMax = globalMax = float('-inf')
        
        for i, v in enumerate(nums):
                # LocalMax becomes the larger of the current number or the current number + localMax itself
                localMax = max(v, v + localMax)

                # If localMax happens to become larger than globalMax, set globalMax to localMax
                if localMax > globalMax: globalMax = localMax
        return globalMax