def subsetSum(nums, sumTo):
    if(len(nums) == 0):
        return 0
    elif(sumTo == 0):
        return 1
    else:
        subsetSum()