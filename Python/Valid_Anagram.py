#Question: Given two words, determine if theyre anagrams
#Solution: Sort and compare
#Difficulty: Easy
#Time Complexity: O(log n) / O(n)
#Space Complexity: O(1) / O(n)

#Trivial solution, sort both strings and compare, complexity is O(log n)
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        