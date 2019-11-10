# Question (#33): Given an array that's sorted but is shifted at a given pivot, find the index of a given number
# Solution: Use a regular binary search, but each time you land on the 'wrong side' of the array from the target, set that
#           value to be + or - infinity and do a regular binary search.
#           The idea is if our array is [5, 6, 7, 8, 1, 2, 3, 4], we can't do a binary search on it because of the rotation,
#           but if we know what side our target is we can make the array [-inf, -inf, -inf, -inf, 1, 2, 3, 4] or [5, 6, 7, 8, inf, inf, inf, inf] 
#           this way we can continue to do a regular binary search.

def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            # If our midpoint is greater than or equal to the starting point, and our target is greater than or equal to the
            # starting point, we know that we've landed in the correct side of the array relative to the target (the left in this case), so don't do
            # anything! 
            if (nums[mid] >= nums[0]) and (target >= nums[0]):               
                pass

            # Conversely, if the mid is less than the start and the target is also less than the start, then we've landed on the correct side (the right side)
            # this is a strict less than comparision and not a less than or equal, because we can only be sure we're on the correct side
            # if the mid is strictly less than the start and so is the target. If we land on the left side and our target is on the right side, this could evaluate to true if it were <=. 
            elif (nums[mid] < nums[0]) and (target < nums[0]):
                pass

            # If we're on the wrong side, check which wrong side it is. If the start is greater than the target, we know we landed 
            # landed on the left side and our target is on the right, so set the current value to be -INF. And vice versa for if the start is 
            # less than the target.
            elif nums[0] > target:
                nums[mid] = float('-inf')
            else:
                nums[mid] = float('inf')
            
            # Do a regular binary search now, since we've updated mid!
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1