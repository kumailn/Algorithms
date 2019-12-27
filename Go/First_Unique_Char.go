import "math"

func firstUniqChar(s string) int {
	type Pair struct {
		count int
		index int
	}

	seen := map[rune]*Pair{}

	for i, v := range s {
		if _, ok := seen[v]; ok {
			seen[v].count++
		} else {
			seen[v] = &Pair{1, i}
		}
	}

	lowest := math.Inf(1)

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