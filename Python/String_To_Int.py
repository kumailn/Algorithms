def toInt(s):
        """
        :type str: str
        :rtype: int
        """
        num = i = 0
        nums = "0987654321"
        s = s.strip(" ")
        if not s: return 0
        neg = s[0] == "-"
        if s[0] == "+" or neg: s = s[1:]
        if not s: return 0
        if s[0] != "-" and s[0] != "+" and s[0] not in nums: return 0
        while i < len(s) and s[i] in nums: i += 1
        if not i and s[i] not in nums: return 0
        num = int(s[:i]) if not neg else - 1 * int(s[:i])
        if num > (2**31) - 1: return (2 ** 31) - 1
        if num < -(2**31): return -1 * (2 ** 31)
        return num
        