# Question: Given a list representing a number add one to it and return as list
# Solution: Loop through list, add 1 if not 9, otherwise change to 0, if head is 0 append 1 to head
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    i = len(digits) - 1

    # Loop through the list backwards, as soon as we see something that's 
    # not a 9 we can increment and return the list. If it's 9 set it to 0
    while i >= 0:
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        i -= 1

    # If we exit the loop without returning that means digits is now
    # an array of all 0s, so just append a 1 at the front and return 
    return [1] + digits