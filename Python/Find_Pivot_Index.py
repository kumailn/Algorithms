# Question: Find the index of the element in the list such that
#           the sum of elements to its left equals the sum of elements to its right
# Difficulty: Easy
# Solution: Store the sum of the left side and right side and adjust each loop and check
# Space Complexity: O(1)
# Time Complexity: O(n)


def pivot(nums):
    if not nums:
        return -1

    leftSum, rightSum = 0, sum(nums)

    for i in range(len(nums)):
        rightSum -= nums[i]
        if(leftSum == rightSum):
            return i

        leftSum += nums[i]

    return -1


def main():
    print(pivot([1, 7, 3, 6, 5, 6]))


main()
