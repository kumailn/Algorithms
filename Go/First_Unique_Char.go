import "math"

func firstUniqChar(s string) int {
	// Create a struct which we can populate our hashmap with
	type Pair struct {
		count int
		index int
	}

	seen := map[rune]*Pair{}

	// Loop over the string, incrementing count if the char exists and adding it othwerwise
	for i, v := range s {
		if _, ok := seen[v]; ok {
			seen[v].count++
		} else {
			seen[v] = &Pair{1, i}
		}
	}

	lowest := math.Inf(1)

	// Loop over the hashmap, and find the minimum index with a count of 1
	for _, v := range seen {
		if v.count == 1 {
			lowest = math.Min(lowest, float64(v.index))
		}
	}

	if lowest == math.Inf(1) {
		return -1
	} else {
		return int(lowest)
	}
}