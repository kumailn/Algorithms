# Question(#347): Given a non-empty array of integers, return the k most frequent elements.
# Solution: Use a counting sort to place the most frequent items into buckets, loop through the buckets backwards,
#           (since the last bucket cooresponds to the most common item), add the items in the bucket to our result and decrement
#           value of k by the amount of items in the bucket

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Make an array with len(nums) + 1 positions, because the max frequency of any element 
    # can coorespond to the len(nums) + 1 index.
    buckets = [[] for _ in range(len(nums) + 1)]
    result = []

    # Save a number to the bucket which cooresponds to its frequency
    for a, b in collections.Counter(nums).items(): buckets[b] += [a]

    # Loop through the buckets backwards, since the ones at the end are the most frequent elements
    for i in buckets[::-1]:
        # If k becomes 0 or negative, we've found enough items
        if k <= 0: return result

        # If there's stuff in the current bucket, add that stuff to our result, and
        # decrement k by the amount of things we just added
        if i:
            result += i
            k -= len(i)

    return result