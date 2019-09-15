# Question: Determing how much rain water is trapped in a stage of blocks 
# Solution: Use two pointers to determine the lower bound and shift accordingly
# Difficulty: Hard

from typing import List

def trap(height: List[int]) -> int:
    water = lastLevel = 0
    left, right = 0, len(height) - 1

    while left < right:
        if height[left] <= height[right]:
            smallerBound = height[left]; left += 1
        else:
            smallerBound = height[right]; right -= 1
        
        if smallerBound > lastLevel: lastLevel = smallerBound
        water += lastLevel - smallerBound
    return water

def main():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))

main()