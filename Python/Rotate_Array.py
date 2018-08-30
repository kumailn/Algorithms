def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nn = nums[:]
    for i in range(k):
        temp = nn[-1]
        nn = [temp] + nn
        del nn[-1]
        print(i, temp, nn)
    nums[:] = nn[:]
    print(nn)
    return None

n = [1,2,3,4,5,6,7]
rotate(n, 3)
print(n)