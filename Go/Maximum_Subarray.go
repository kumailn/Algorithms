import "math"

func maxSubArray(nums []int) int {
	localMax, globalMax := math.Inf(-1), math.Inf(-1)

	for _, v := range nums {
		localMax = math.Max(localMax+float64(v), float64(v))
		globalMax = math.Max(globalMax, localMax)
	}

	return int(globalMax)
}