# Question[#50]: Given a number, compute its power
# Difficulty: Medium
# Solution: Use recursion to break the computation into halves each time to achieve O(log n)


def myPow(x: float, n: int) -> float:
    # Our base case, anything ^ 0 = 1
    if n == 0:
        return 1

    # If our power is negative, simply invert the number and make the power positive
    if n < 0:
        x = 1/x
        n *= -1

    # If the power is even we want to compute the number times itelf with half the power
    # ie (3^8 == (3^2^4) == (3*3)^4)) and if its odd we multiply it with itself but with a power of one less
    return self.myPow(x*x, n // 2) if n % 2 == 0 else self.myPow(x, n - 1) * x
