#Question: Given a list representing a number add one to it and return as list
#Solution: Loop through list, add 1 if not 9, othersie change to 0, if head is 0 append 1 to head
#Difficulty: Easy

def plusOne(nums):
    #Let head be first item in list
    head = nums[0]
    #Let i be last index
    i = -1
    #While last index is 9, change it to 0, move last index up left
    while nums[i] == 9:
        nums[i] = 0
        if (i != -len(nums)): i -= 1
    #If i has reached head and head is 9, add 1 to front of nums
    if(i == -len(nums) and head == 9): nums = [1] + nums
    #Otherwise just add 1 to the number i got up to
    else: nums[i] += 1
    return nums

print(plusOne([1, 2, 3, 4, 0]))
print(plusOne([9, 9]))
print(plusOne([9, 9, 5, 9]))