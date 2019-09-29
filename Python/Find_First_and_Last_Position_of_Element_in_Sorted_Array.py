# Question: Given a sorted array, find the first and last indices of a target number
# Solution: Run two (lower bounded) binary searches, one for the target number and one 
#           for the successor of the target (the next natural number after the targer number)
# Difficulty: Medium

def searchRange(nums: List[int], target: int) -> List[int]:

    def lowerBin(nums, target):
        l, r = 0, len(nums) - 1

        # Note: setting this while statement to be <= and not just != means it can also
        # catch cases when the input is an empty array, as l = 0 and r = -1 in that case
        while l <= r:

            # In each iteration set the midpoint to half the difference of the left 
            # and right pointers offset by the left pointer
            mid = (r - l) // 2 + l

            # This binary search always returns the lower bound on a number because
            # if the current number is less than target it shifts left to the next number to the right of mid,
            # and if the number is greater than or equal to the target it shifts right to the number to the left of mid
            # this ensures that if numbers are duplicated the search will always narrow into the leftmost number
            if nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return l
                
    # This simply finds the index of the lowest target
    lowerIndex = lower(nums, target)

    # This finds the index of the first number larger than the target, and then subtracts 
    # one from the index it finds which is going to be the rightmost target 
    upperIndex = lower(nums, target + 1) - 1
        
    # If we didn't go out of bounds in our search and if the number at the lowerIndex actually equals our
    # target (because our binary search will return the next largest number if it didn't exist) we can return the indices
    if lowerIndex < len(nums) and nums[lowerIndex] == target: 
        return [lowerIndex, upperIndex]
    else: return [-1, -1]