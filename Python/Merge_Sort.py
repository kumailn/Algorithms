def sortMerge(nums):
    #Our base case, if the list is 1 item long we can return itself because it's already sorted
    if len(nums) == 1: return nums

    #Recursively merge sort left and right lists
    left = sortMerge(nums[:len(nums) // 2])
    right = sortMerge(nums[len(nums) // 2:])

    sortedNums, i, j = [], 0, 0

    #While i and j are less than he lengths of each of their lists
    while i < len(left) and j < len(right):
        #Add the smaller item in the left list or right list and increment our counter
        if left[i] < right[j]: 
            sortedNums += [left[i]]; i += 1
        else:
            sortedNums += [right[j]]; j += 1

    #Add the rest of the numbers as we've exhausted one of the lists
    sortedNums += left[i:] + right[j:]

    return sortedNums

def main():
    nums = [6, 7, 3, 2, 9, 3, 1, 0]
    print(sortMerge(nums))

main()