#Question: Given two words, determine if theyre anagrams
#Solution: Sort and compare
#Difficulty: Easy


def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        