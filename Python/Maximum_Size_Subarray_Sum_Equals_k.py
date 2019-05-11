#Question: Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
#Solution: Keep a hashmap of sums up to that point 
#Difficulty: Medium
#Space Complexity: O(n)
#Time Complexity: O(n)

from typing import List

def maxSubArrayLen(nums: List[int], k: int):
    #Initialize values for the max sub-array itself and it's value
    answer, accumulator = [], 0
    
    #Create a hashmap with keys being sums and values indexes, sum at index -1 is 0
    #This is important because if the accumulator sums to 0 at any point we can use this 0 and include all numbers from the beginning
    sumMap = {0: -1}

    for i, v in enumerate(nums):
        #Increment the accumulator by the number in the array
        accumulator += v

        #If we haven't previously encountered this number, add it to hashmap with index i
        if accumulator not in sumMap: sumMap[accumulator] = i

        #If the accumulator - the k we're looking for happens to be in our map
        #This is because accumulator - (accumulator - k) = k. In other words the accumulator up to this point, subtracted by the (accumulator-k) must be k
        if accumulator - k in sumMap: 

            #If the length of k is greater than the length of our answer, because k spans from index at sum accumulator - k to index at i (from the above comment)
            if (i - sumMap[accumulator - k]) > len(answer): 

                #Set answer to be the subarray starting from the inde of the sum (accumulator-k) to i inclusively
                #We want the starting point to be non-inclusive of the last item in the sum (accumulator-k) because we need to subtract this sum completely...
                #..from the current accumulator in order to obtain k. (Since accumulator - (accumulator - k) = k)
                answer = nums[sumMap[accumulator-k]+1:i+1]
    return answer
    

def main():
    print(maxSubArrayLen([1, 1, 2, 3, -1, 0, -1, 1, 2, 3], 5))
    print(maxSubArrayLen([-2, -1, 2, 1, 9], 9))
main()