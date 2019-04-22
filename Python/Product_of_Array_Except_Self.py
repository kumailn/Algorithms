#Question: Given a list of numbers, multiply each number by all other numbers except itself
#Solution: Traverse right then left while multiplying
#Difficulty: Medium
#Time Complexity: O(n)
#Space Complexity: O(n)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    #Initialize a variable to store the current multiplication, and one to store the result
    multiplier, result = 1, [1] * len(nums)

    #Loop through forwards
    for i, v in enumerate(nums):

        #Set the ith index to be the multiplier, and multiply the multiplier by the current number
        result[i] *= multiplier
        multiplier *= v

    #Reset the multiplier
    multiplier = 1
    
    #Loop through backwards doing the same thing
    for i, v in reversed(list(enumerate(nums))):
        result[i] *= multiplier
        multiplier *= v
    
    return result


def main():
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([4,3,2,1,2]))
main()
