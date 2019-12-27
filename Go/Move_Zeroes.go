func moveZeroes(nums []int) {
	notZeroIndex := 0

	for i, v := range nums {
		if v != 0 {
			nums[i], nums[notZeroIndex] = nums[notZeroIndex], nums[i]
			notZeroIndex++
		}
	}
}