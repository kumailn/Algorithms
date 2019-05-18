// Question: Given a list of ints, find the smallest missing positive number
// Solution: Sort the list as you go through by placing every term on its index + 1th place.
// Difficulty: Hard 
// Time Complexity: O(n)
// Space Complexity: O(1)

fun firstMissingPositive(nums: IntArray): Int {
    var left = 0;
    var right = nums.size;
    
    while (left < right) {
        // If the current number is equal to its index + 1, skip over as its already sorted
        // for example if the number 5 is in the 4th index/ 5th place
        if (nums[left] == left + 1) left++;

        // Otherwise, if  number not in the correct place
        // In othe words, if a number n is within our range and the number in the nth position isnt equal to this number, swap the two
        else if (nums[left] > 0 && nums[left] <= nums.size && nums[left] != nums[nums[left]-1]) {
            nums[nums[left]-1] = nums[left].also{ nums[left] = nums[nums[left]-1] };
        } 
        
        // Case if the number is a duplicate, or out of our range (1 to right). So place it at the end 
        else nums[left] = nums[--right].also{ nums[right] = nums[left] };   
    }
    return right + 1;
}

fun main(args: Array<String>) { 
    var arr: IntArray = intArrayOf(7,8,9,11,12);
    print(firstMissingPositive(arr));
}