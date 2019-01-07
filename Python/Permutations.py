def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        def rec(nums, r, current):
            if not nums: r += [current]
            for i in range(len(nums)):
                rec(nums[:i] + nums[i+1:], r, current + [nums[i]])
            return r
        return(rec(nums, r, []))