#Question: Given a sorted list of numbers, find two numbers that add to a given target
#Solution: Keep left and right pointers and adjust accordingly
#Difficulty: Easy 

def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #left and right pointers
        l, r = 0, len(numbers) - 1
        #while left is less than right
        while l < r:
            #If left + right is the target return them
            if numbers[l] + numbers[r] == target: return [l, r]
            #If its more then the target we need to find smaller numbers to add so move right pointer down
            elif numbers[l] + numbers[r] > target: r -= 1
            #If its more move left pointer up
            else: l += 1
        return []