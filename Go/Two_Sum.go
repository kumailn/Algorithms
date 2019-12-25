func twoSum(nums []int, target int) []int {
	lookingFor := map[int]int{}
	for i, v := range nums {
		if val, ok := lookingFor[v]; ok {
			return []int{val, i}
		}
		lookingFor[target-v] = i
	}
	return []int{-1, -1}
}