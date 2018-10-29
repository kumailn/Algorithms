#Question: Given a string, find the first character that is unique
def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d: d[i] += 1
            else: d[i] = 1
        for i, v in enumerate(s):
            if d[v] == 1: return i
        return -1