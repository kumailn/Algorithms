#Question: Count the number of pairs that add to a given value
#Solution: Modifiy a traditional two sum
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(n)

def twoAll(nums, target):
    #Keep a hashmap of the counts of our new targets 
    counts = {}
    #Keep a variable to store all pair counts
    count = 0
    for i, v in enumerate(nums):
        #If the current number in our nums array is present in our counts hashmap, then increment our count variable by the number of times it's been seen so far
        if v in counts: count += counts[v]
        #Update our counts hashmap and increment the count of our new target (target - v) by 1
        counts[target - v] = counts.get(target - v, 0) + 1
    return count




def main():
    nums = [2, 3, 1, 3, 2, 1]
    nums2 = [1, 1, 1, 1, 1, 2, 0, 3, 0]
    print(twoAll(nums, 5))
    print(twoAll(nums2, 3))
main()