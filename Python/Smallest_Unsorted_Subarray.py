#Question: Given an array, find the length of the smallest subarray such that if you sort the subarray the entire array becomes sorted 
#Solution: Sort array and see differences, (Naive approach)


#Naive approach
def findUnsortedSubarrayN(arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmin, cmax, end, beg = arr[-1], arr[0], -2, -1
        for i in range(1, len(arr)):
            cmax = max(cmax, arr[i])
            cmin = min(cmin, arr[len(arr) - 1 - i])
            if arr[i] < cmax: end = i
            if arr[len(arr) - 1 - i] > min: beg = len(arr) - 1 - i
        return end - beg + 1

#Optimal approach
def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = -1, 0
        mmin, mmax = float('inf'), float('-inf')
        for i in range(len(nums)):
            mmax = max(mmax, nums[i])
            if nums[i] != mmax: l = i
                
            mmin = min(mmin, nums[len(nums) - i - 1])
            if nums[len(nums) - i - 1] != mmin: r = len(nums) - i - 1
        print(l, r)
        return l - r + 1
            
            

def main():
    a = [1, 4, 6, 8, 3, 2, 9]
    arr = [2,6,4,8,10,9,15]

    print(smallesUnsortedSubarray(a))
    print(smallesUnsortedSubarray(arr))

main()