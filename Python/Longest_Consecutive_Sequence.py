# Question(#128): Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Difficulty: Hard


def longestConsecutive(self, nums: List[int]) -> int:
    # Turn nums into a set so lookups happen in constant time
    nums = set(nums)
    longest = 0

    for a in nums:
        # If a smaller number does not exist, we know this is the smallest in
        # the potential sequence of consecutive elements and we can just check for larger nums
        if a - 1 not in nums:
            b = a + 1
            # As long as a number 1 greater exists, we can keep checking for the next
            # consecutive element in the set, longest will then just be the max of the distances
            while b in nums:
                b += 1
            longest = max(longest, b - a)

    return longest
