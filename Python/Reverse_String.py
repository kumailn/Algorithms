#Question: Reverse a string
#Solution: Swap left and right pointers
#Difficulty: Easy

def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(len(s) // 2): s[i], s[-i - 1] = s[-i - 1], s[i]
        return "".join(s)