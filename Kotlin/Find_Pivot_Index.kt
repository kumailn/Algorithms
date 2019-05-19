// Question: Find the index of the element in the list such that 
//           the sum of elements to its left equals the sum of elements to its right
// Difficulty: Easy
// Solution: Store the sum of the left side and right side and adjust each loop and check
// Space Complexity: O(1)
// Time Complexity: O(n)

fun pivotIndex(nums: IntArray): Int {
    var leftSum = 0;
    var rightSum = nums.sum();

    for(i in 0 until nums.size) {
        rightSum -= nums[i];
        if (leftSum == rightSum) return i;
        leftSum += nums[i];
    }
    return -1;
}

fun main(args: Array<String>) {
    var nums: IntArray = intArrayOf(1, 7, 3, 6, 5, 6);
    print(pivotIndex(nums));
}