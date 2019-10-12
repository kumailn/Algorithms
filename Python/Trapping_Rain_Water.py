# Question: Determing how much rain water is trapped in a stage of blocks
# Solution: Use two pointers to determine the lower bound and shift accordingly
# Difficulty: Hard


def trap(height: List[int]) -> int:
    water = smaller = depth = 0
    l, r = 0, len(height) - 1

    while l < r:
        # Set 'smaller' to be the smaller height of the two pointers, and shift pointers accordingly
        if height[l] < height[r]:
            smaller = height[l]
            l += 1
        else:
            smaller = height[r]
            r -= 1

        # Set depth to be the largest lower bound we've encountered so far
        # this will be the upper bound of the level of the water
        depth = max(depth, smaller)

        # The water level per block will simply be the depth we've computed minus the smaller bound we're currently at
        water += depth - smaller
    return water
