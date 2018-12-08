#Question: Count the number of pairs that add to a given value
#Solution: Modifiy a traditional two sum
#Difficulty: Easy

def twoAll(nums, target):
    counts = {}
    count = 0
    for i, v in enumerate(nums):
        if v in counts: count += counts[v]
        counts[target - v] = counts.get(target - v, 0) + 1
    return count




def main():
    nums = [2, 3, 1, 3, 2, 1]
    nums2 = [1, 1, 1, 1, 1, 2, 0, 3, 0]
    print(twoAll(nums, 5))
    print(twoAll(nums2, 3))
main()