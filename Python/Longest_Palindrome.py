#Question: Given a string, find the longest palindrome you can construct using its letters
#Solution: Add together all counts of letters, if an odd count exists then add count - 1 otherwise count, return 1 + total if an odd existed because it can be used in the middle.
#Difficulty: Easy

def longestPalindrome(s):
        """
        :type s: str
        :rtype: int
        """
        #Dictionary to keep count of each character
        counts = {}
        #Total count to return 
        count = 0
        #Bool to remember if an odd count of numbers is found 
        oddFound = False
        #Count each character, store in dictionary 
        for i, v in enumerate(s):
            counts[v] = counts.get(v, 0) + 1
        #For every character we counted 
        for char in counts:
            #If it occurs an odd number of times set oddFound flag to true
            if counts[char] % 2 == 1: oddFound = True
            #Increase total by occurence of current letter if its count is even, otherwise subtract 1 from its occurance
            count += counts[char] if counts[char] % 2 == 0 else counts[char] - 1
        return count + 1 if oddFound else count
        