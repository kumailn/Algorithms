def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        countMap = {0: 1}
        current = 0
        result = 0
        for i in nums:
            current += i
            result += countMap[current - k] if (current - k) in countMap else 0
            countMap[current] = countMap.get(current, 0) + 1
        print(countMap)
        return result