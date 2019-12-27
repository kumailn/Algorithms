func isValid(s string) bool {
	stack := []rune{}
	complement := map[rune]rune{
		'}': '{',
		')': '(',
		']': '[',
	}

	for _, v := range s {
		if v == '(' || v == '[' || v == '{' {
			stack = append(stack, v)
		} else if len(stack) != 0 && stack[len(stack)-1] == complement[v] {
			stack = stack[:len(stack)-1]
		} else {
			return false
		}
	}

	return len(stack) == 0
}