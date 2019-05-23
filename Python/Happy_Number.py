# Question: See https://leetcode.com/problems/happy-number/
# Difficulty: Easy
# Solution: Maintain a set of already seen numbers and loop
# Space Complexity: O(n)
# Time Complexity: O(n)


def isHappy(n: int) -> bool:
    seen = set()
    while n != 1:
        seen.add(n)
        n = sum(map(lambda x: int(x) ** 2, list(str(n))))
        if n in seen:
            return False
    return True


def main():
    print(isHappy(19))


main()
