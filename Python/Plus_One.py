#Question: Given a list representing a number add one to it and return as list
#Solution: Loop through list, add 1 if not 9, othersie change to 0, if head is 0 append 1 to head
#Difficulty: Easy

def plusOne(nums):
    #Initialize pointer to the last element of the numbers 
    i = len(nums) - 1
    #As long as the item at the pointer is 9, set it to 0
    while nums[i] == 9: nums[i] = 0; i -= 1
    #If the first number has become 0 after our above loop, then append 1 to the front of nums
    if nums[0] == 0: nums = [1] + nums
    #Otherwise just add 1 to where the pointer stopped at   
    else: nums[i] += 1
    return nums
    


print(plusOne([1, 2, 3, 4, 0]))
print(plusOne([9, 9]))
print(plusOne([9, 9, 5, 9]))
print(plusOne([0]))