// Question: Given a list representing a number add one to it and return as list
// Solution: Loop through list, add 1 if not 9, otherwise change to 0, if head is 0 append 1 to head
// Difficulty: Easy
// Time Complexity: O(n)
// Space Complexity: O(1)

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}

	return append([]int{1}, digits...)
}