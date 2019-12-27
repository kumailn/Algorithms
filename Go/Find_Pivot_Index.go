func pivotIndex(nums []int) int {
	if len(nums) == 0 {
		return -1
	}

	left := 0
	right := 0
	for _, v := range nums {
		right += v
	}

	for i, v := range nums {
		right -= v
		if left == right {
			return i
		}
		left += v
	}

	return -1
}