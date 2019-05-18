#Question: Given a list of ints, find the smallest missing positive number
#Solution: Sort the list as you go through by placing every term on its index + 1th place.
#Difficulty: Hard 
#Time Complexity: O(n)
#Space Complexity: O(1)

from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    i, j = 0, len(nums)
    while i < j:

        #If the current number is equal to its index + 1, skip over as its already sorted
        #for example if the number 5 is in the 4th index/ 5th place
        if nums[i] == i+1: i += 1

        #Regular case, ie a number not in the correct place
        #In othe words, if a number n is within our range and the number in the nth position isnt equal to this number, swap the two
        elif nums[i] > 0 and nums[i] <= j and nums[nums[i]-1] != nums[i]: 
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        #Case if the number is a duplicate, or out of our range (1 to j). So place it at the end 
        else: 
            j -= 1
            nums[j], nums[i] = nums[i], nums[j]

    return j + 1
                
def main():
    print(firstMissingPositive([1, 5, 4, 3, 2, 7, 0]))

main()