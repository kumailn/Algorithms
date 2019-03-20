#Question: Move 0s to the end of a list
#Difficulty: Easy
#Solution: Keep an index to place non zeros at and keep incrementing it each time you encounter a non zero
#Space Complexity: O(1)
#Time Complexity: O(n)

from typing import List
def moveZeroes(nums: List[int]) -> None:
        nonZeroIndex = 0

        #Loop through
        for i, v in enumerate(nums):
            #If the element is not 0, swap it with the item at 'nonZeroIndex' and increment 'NnonZeroIndex'
            if v != 0:
                nums[i], nums[nonZeroIndex] = nums[nonZeroIndex], nums[i]
                nonZeroIndex += 1
    
def main():
    a = [0, 4, 0, 4, 2, 0, 9]
    moveZeroes(a)
    print(a)

main()