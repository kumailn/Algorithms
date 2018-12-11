    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or not nums: return 0
        lookingFor = {}; pairs = 0
        for i in range(len(nums)):
            lookingFor[nums[i]] = lookingFor.get(nums[i], 0) + 1
        for i in lookingFor:
            if k == 0:
                if lookingFor[i] > 1: 
                    pairs += 1
            else:
                if k + i in lookingFor: 
                    pairs += 1
        return pairs