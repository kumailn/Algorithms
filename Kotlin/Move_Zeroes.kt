// Question: Move 0s to the end of a list
// Difficulty: Easy
// Solution: Keep an index to place non zeros at and keep incrementing it each time you encounter a non zero
// Space Complexity: O(1)
// Time Complexity: O(n)

fun moveZeroes(nums: IntArray): Unit {
    //Initialize index to store numbers that aren't 0s
    var nonZeroIndex = 0;
    for(i in 0 until nums.size) {
        
        //Everytime a non zero is encountered, swap it with the item at the place of index 'nonZeroIndex' and increment
        if (nums[i] != 0) nums[nonZeroIndex] = nums[i].also{nums[i] = nums[nonZeroIndex++]};   
    }
}

fun main(args: Array<String>) {
    val numbers: IntArray = intArrayOf(3, 2, 0, 6, 0, 8)
    moveZeroes(numbers);
    print(numbers.joinToString());
}