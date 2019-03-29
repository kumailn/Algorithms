/* Question: Move 0s to the end of a list
Difficulty: Easy
Solution: Keep an index to place non zeros at and keep incrementing it each time you encounter a non zero
Space Complexity: O(1)
Time Complexity: O(n) */

List<int> moveZeroes(List<int> nums) {
  int nonZeroIndex = 0;
  for (int i = 0; i < nums.length; i++) {
    if (nums[i] != 0) {
      int swap = nums[i];
      nums[i] = nums[nonZeroIndex];
      nums[nonZeroIndex++] = swap;
    }
  }

  return nums;
}

main(List<String> args) {
  List<int> nums = [1, 0, 0, 4, 5, 0];
  print(moveZeroes(nums));
}