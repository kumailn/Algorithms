#Question: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#Solution: Keep a hashmap with keys of target - num
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(n)

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    #Create a hashmap to store numbers we want to look for
    lookingFor = {}
    for i, v in enumerate(nums):
        #If the number we're at is one we're looking for
        #Return it's index along with the one in the hashmap
        if v in lookingFor: return [lookingFor[v], i]
        
        #Otherwise we want to look for the target - current number
        lookingFor[target - v] = i
            

def main():
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))

main()
