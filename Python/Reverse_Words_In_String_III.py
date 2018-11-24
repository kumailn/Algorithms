#Question: Given a string, reverse each word in the string
#Solution: Reverse each word in the string using a helper function
#Difficulty: Easy

def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        def rev(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                r -= 1
                l += 1
        l, r = 0, 0
        while r < len(s): 
            r += 1
            if r == len(s) or s[r] == " ":
                rev(s, l, r - 1)
                l = r + 1
                r += 1
        return "".join(s)