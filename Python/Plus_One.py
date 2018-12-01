#Question: Given a list representing a number add one to it and return as list
#Solution: Loop through list, add 1 if not 9, othersie change to 0, if head is 0 append 1 to head
#Difficulty: Easy

def plusOne(nums):
    for i in range(len(nums))[::-1]:
        if nums[i] != 9: 
            nums[i] += 1
            return nums
        else: 
            nums[i] = 0
    return [1] + nums


print(plusOne([1, 2, 3, 4, 0]))
print(plusOne([9, 9]))
print(plusOne([9, 9, 5, 9]))
print(plusOne([0]))