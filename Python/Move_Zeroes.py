#Question: Move 0s to the end of a lists
def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i, v in enumerate(nums):
            if v != 0:
                nums[i], nums[z] = nums[z], nums[i]
                z += 1