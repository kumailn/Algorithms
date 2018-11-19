#Question: Given a list of ints, find the smallest missing positive number
#Solution: Find the smallest positive number, if its 1 go up until you find missing one, else return 1
#Difficulty: Easy 

def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Initialize our compare variable to infinity
        c = float('inf')
        for i in range(len(nums)):
            #If nums[i] is less than our counter and its positive, set counter to nums[i]
            if nums[i] < c and nums[i] > 0: c = nums[i]
        #If c isnt 1, then return 1
        if c != 1: return 1
        while c in nums: c += 1
        #If c is 1, add up until you find a number not in the list
        return c
            