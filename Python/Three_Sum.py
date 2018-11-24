#Question: Find 3 unique numbers that add to a given newTarget number
#Solution: Sort list first then move pointers accordingly to find a number that sums to newTarget
#Difficulty: Medium 
#Complexity: O(N) = O(N + NLog(N))


def threeSum(nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #The set of possible solutions
        solutions = []
        #Sort the numbers array, this uses NlogN complexity
        nums = sorted(nums)
        #Loop up till the 3rd last element! This is beacuse the last possible solution set starts at the third last element
        for i in range(len(nums) - 2):
            #If i is not 0, and i is the same as the previous i, skip this loop iteration
            if i and nums[i] is nums[i - 1]: continue
            #Initialize the left pointer, right pointer to be i + 1 (next value) and len(n) - 1 (last value). Initialize a newtarget we're looking for, which is the original target minus the current number we're at in the loop
            l, r, newTarget = i + 1, len(nums) - 1, target - nums[i]
            #While left pointer is less than right pointer
            while l < r:
                #If the numbers at the left and right pointer sum to the new target, add that solution to our result!
                if nums[l] + nums[r] == newTarget:
                    solutions += [[nums[r], nums[l], nums[i]]]
                    #Increace l as long as its equal to its previous value, and vice versa for r
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    #Increase and decrease l and r
                    l += 1; r -= 1
                #If the left and right poniters add to less than our sum, we know we can shift the left pointer up because the list is sorted!
                elif nums[l] + nums[r] < newTarget: l += 1
                #If they they add to a smaller number move right pointer down
                else: r -= 1
        return solutions