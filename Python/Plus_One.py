#Question: Given a list representing a number add one to it and return as list
#Solution: Loop through list, add 1 if not 9, otherwise change to 0, if head is 0 append 1 to head
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(1)

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    #Loop through backwards, if we reach a 9 set it to 0, otherwise increment and return
    for i in range(len(digits))[::-1]:
        if digits[i] == 9: 
            digits[i] = 0
        else: 
            digits[i] += 1
            return digits
    #If we've exhausted the above loop, we must've reached a number beginning in 9, so append 1 to the front
    return [1] + digits


print(plusOne([1, 2, 3, 4, 0]))
print(plusOne([9, 9]))
print(plusOne([9, 9, 5, 9]))
print(plusOne([0]))