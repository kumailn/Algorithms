def maxSubArrayLen(nums, k):
    answer, accumulator = [], 0
    sumMap = {0:-1}
    for i,v in enumerate(nums):
        accumulator += v
        if accumulator not in sumMap: sumMap[accumulator] = i
        print(sumMap, accumulator-k)
        if accumulator-k in sumMap: 
            if (i - sumMap[accumulator - k]) > len(answer): answer = nums[sumMap[accumulator-k]+1:i+1]
    return answer
    

def main():
    print(maxSubArrayLen([-2, -1, 2, 1, 9], 9))
main()