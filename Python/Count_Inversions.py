def countInversions(nums):
    #Our recursive base case, if our list is of size 1 we know there's no inversion and that it's already sorted
    if len(nums) == 1: return nums, 0

    #We run our function recursively on it's left and right halves
    left, leftInversions = countInversions(nums[:len(nums) // 2])
    right, rightInversions = countInversions(nums[len(nums) // 2:])

    #Initialize our inversions variable to be the number of inversions in each half
    inversions = leftInversions + rightInversions

    #Initialize a list to hold our sorted result list
    sortedNums = []

    i = j = 0
    #Here we count the inversions that exist between the two halves -- while sorting them at the same time
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedNums += [left[i]]; i += 1
        else:
            sortedNums += [right[j]]; j += 1

            #Since we know that 'left' is sorted, once we reach an item in 'left' thats bigger than something in right that item and everything to it's right-hand side must be an inversion!
            #This line right here is exactly what shrinks the time of this algorithm from n^2 to nlogn as it means we don't need to compare every single pair
            inversions += len(left) - i

    #Once we've exhausted either left or right, we can just add the other one onto our sortedNums list
    sortedNums += left[i:] + right[j:]

    return sortedNums, inversions


def main():
    nums = [1, 5, 4, 8, 10, 2, 6, 9]
    print(countInversions(nums))

main()