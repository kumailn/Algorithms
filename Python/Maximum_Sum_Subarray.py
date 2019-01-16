#Question: Find the sum of a continious subarray in an array with the largest sum
#Solution: Kadanes algorithm (explained below)
#Difficulty: Easy
#Time Complexity: O(n)
   
def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Trivial case
        if not nums: return 0

        #Initialize a store for the local and global maximum sumarrays
        localMax = globalMax = nums[0]

        #Start looping through the numbers from index 1 because local and gloval are nums[0]
        for i in range(1, len(nums)):
            #LocalMax becomes the larger of the current number or the current number + localMax itself
            localMax = max(localMax + nums[i], nums[i])

            #If localMax happens to become larger than globalMax, set globalMax to localMax
            if localMax > globalMax:
                globalMax = localMax

        return globalMax

def main():
    #Result should be 6
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

main()