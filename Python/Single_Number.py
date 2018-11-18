#Question: Given a list of numbers where every number is repeted twice except one, find that number
#Solution: XOR every number together, words because XOR is commutative and a number XOR itself is 0
#Difficulty: Easy

def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums: r ^= i
        return r