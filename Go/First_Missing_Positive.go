// Question: Given a list of ints, find the smallest missing positive number
// Solution: Sort the list as you go through by placing every term on its index + 1th place.
// Difficulty: Hard
// Time Complexity: O(n)
// Space Complexity: O(1)

func firstMissingPositive(nums []int) int {
    i := 0
	j := len(nums)

	for i < j {
        predecessor := nums[i]-1

		// Shift up if the current number is in the correct order (eg. if 5 is in index 4)
		if nums[i] == i+1 {
			i++
		}

		// If num is within range but its in the wrong spot swap it
		// eg. If current num is 5 but nums[5-1] or nums[4] isn't 5
		else if (nums[i] > 0 && nums[i]) <= j && nums[predecessor] != nums[i] {
			tmp := nums[i]
            nums[i] = nums[predecessor]
            nums[predecessor] = tmp
		}

		// If the above checks fail we have a duplicate or num out of range
		// place at end and shrink the bounds
		else {
			j -= 1
			tmp := nums[i]
			nums[i] = nums[j]
			nums[j] = tmp
		}
	}

	return j + 1
}