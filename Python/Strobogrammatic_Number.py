def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n2 = ""
        updowns = {"6": "9", "8": "8", "9": "6", "0":"0", "1":"1"}
        if "7" in num or "5" in num or "3" in num or "4" in num or "2" in num: return False
        for i, v in enumerate(num[::-1]):
            n2 += updowns[v]
        print(n2)
        return num == n2