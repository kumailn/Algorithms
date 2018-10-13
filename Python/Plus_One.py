def plusOne(nums):
    head = nums[0]
    i = len(nums) - 1
    if(nums[i] != 9):
        nums[i] += 1
        return nums
    while nums[i] == 9:
        nums[i] = 0
        if (i - 1 >= 0): i -= 1
    if(i == 0 and head == 9): nums = [1] + nums
    else: nums[i] += 1
    return nums

print(plusOne([1, 2, 3, 4, 0]))
print(plusOne([9, 9]))