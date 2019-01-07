def findClosestElements(arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        #Set left and right pointers, right is k less than len
        left, right = 0, len(arr) - k
        #As long as left is less than right
        while left < right:
            #Find the mid point of left and right
            mid = (left + right) // 2
            #If the mid point less targer is greater than 
            if (x - arr[mid]) > (arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

def insertSorted(arr, x):
    i = 0
    while i < len(arr):
        if arr[i] >= x:
            arr.insert(i, x)
            return arr
        i += 1
    return arr + [x]

print(findClosestElements([1, 2, 3, 4, 5, 6], 2, 3))
print(insertSorted([1, 2, 3, 4, 5], 0.4))